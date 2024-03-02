from csv import writer
import pandas as pd
import io
from datetime import datetime, timedelta
import tabula
import random
import numpy as np
from dateutil import parser
import os
dir_path = os.path.dirname(os.path.realpath(__file__))

class Processing:
    def __init__(self, arr):
        self.source=arr
    def data_merge_simple(self):
        final_df = pd.read_csv("Final_Merged.csv")

        # 2. Load each of the three new USGS files
        usgs_1800_1849 = pd.read_csv(self.source[0])
        usgs_1850_1899 = pd.read_csv(self.source[1])
        usgs_1900_1949 = pd.read_csv(self.source[2])

        # 3. Append each of these to the final_df
        for df in [usgs_1800_1849, usgs_1850_1899, usgs_1900_1949]:
            temp = df[['time', 'mag', 'longitude', 'latitude', 'depth']]
            temp.columns = ['DateTime', 'Magnitude', 'Longitude', 'Latitude', 'Depth']
            final_df = final_df._append(temp, ignore_index=True)

        # 4. Save the updated final_df
        final_df.to_csv("Final_Merged_Updated.csv", index=False)
    def data_merge(self):
        #This code is for when you are checking for duplicate earthquakes

        # 1. Load the USGS files and concatenate them
        usgs_2000_2023 = pd.read_csv(os.path.join(dir_path, self.source[0]))
        usgs_1950_1999 = pd.read_csv(os.path.join(dir_path, self.source[1]))

        usgs = pd.concat([usgs_1950_1999, usgs_2000_2023], ignore_index=True)

        # 2. Load the SAGE file
        sage = pd.read_csv(os.path.join(dir_path, self.source[2]), delimiter='|', skiprows=4)

        # 3. Use a two-pointer approach
        i, j = 0, 0
        result = []

        while i < len(usgs) and j < len(sage):
            usgs_time = pd.Timestamp(usgs.iloc[i]['time'])
            sage_time = pd.Timestamp(sage.iloc[j]['Time'])

            if abs((usgs_time - sage_time).total_seconds()) <= 10:
                if (abs(usgs.iloc[i]['latitude'] - sage.iloc[j]['Latitude']) <= 0.1 and
                    abs(usgs.iloc[i]['longitude'] - sage.iloc[j]['Longitude']) <= 0.1 and
                    abs(usgs.iloc[i]['mag'] - sage.iloc[j]['Magnitude']) <= 0.2):
                    
                    # Consider as the same earthquake, choose randomly
                    if random.choice([True, False]):
                        result.append([usgs_time, usgs.iloc[i]['mag'], usgs.iloc[i]['longitude'], usgs.iloc[i]['latitude'], usgs.iloc[i]['depth']])
                    else:
                        result.append([sage_time, sage.iloc[j]['Magnitude'], sage.iloc[j]['Longitude'], sage.iloc[j]['Latitude'], sage.iloc[j]['Depth']])
                    
                    i += 1
                    j += 1
                    continue
            if usgs_time < sage_time:
                result.append([usgs_time, usgs.iloc[i]['mag'], usgs.iloc[i]['longitude'], usgs.iloc[i]['latitude'], usgs.iloc[i]['depth']])
                i += 1
            else:
                result.append([sage_time, sage.iloc[j]['Magnitude'], sage.iloc[j]['Longitude'], sage.iloc[j]['Latitude'], sage.iloc[j]['Depth']])
                j += 1

        # 4. Convert the result list to DataFrame and export it
        result_df = pd.DataFrame(result, columns=['DateTime', 'Magnitude', 'Longitude', 'Latitude', 'Depth'])
        result_df.to_csv("Final_Merged.csv", index=False)
    
    def syria_cleaning(self):
        # Read the CSV file into a Pandas DataFrame
        input_file = self.source[0]  # Replace with the actual file path
        output_file = self.source[1]    # Replace with the desired output file path

        df = pd.read_csv(input_file)

        # Drop unnecessary columns
        df = df.drop(columns=['No.', 'Major affected localities', 'I0', 'H'])

        # Changed column names
        column_mapping = {'Date':'DateTime', 'Lat.': 'Latitude', 'Long.': 'Longitude', 'Ms':'Magnitude'}
        df = df.rename(columns=column_mapping)

        default_datetime = datetime(year=1900, month=12, day=29)

        def convert_datetime(input_date):
            date_object = parser.parse(input_date, default=default_datetime)
            standard_format = date_object.strftime('%Y-%m-%d %H:%M:%S.%f+00:00')
            return standard_format

        def clean(input):
            if input == '-':
                output = np.nan
            else:
                output = input
            return output


        df['DateTime'] = df['DateTime'].apply(convert_datetime)
        df['Latitude'] = df['Latitude'].apply(clean)
        df['Longitude'] = df['Longitude'].apply(clean)
        df['Magnitude'] = df['Magnitude'].apply(clean)

        # Save the results to a new CSV file
        df.to_csv(output_file, index=False)

        print(f"Conversion completed. Results saved to {output_file}")

    def usgs_sage_merge(self):
        # Load data
        usgs_df = pd.read_csv(self.source[0], parse_dates=['time'])
        sage_df = pd.read_csv(self.source[1], delimiter='|', comment='#', skipinitialspace=True, parse_dates=['Time'])

        # custom function to identify same event 
        def is_same_event(row):
            for idx, sage_row in sage_df.iterrows():
                time_diff = abs((row['time'] - sage_row['Time']).total_seconds())
                lat_diff = abs(row['latitude'] - sage_row['Latitude'])
                long_diff = abs(row['longitude'] - sage_row['Longitude'])

                # Change this numbers to change how we define same events 
                if time_diff <= 10 and lat_diff <= 0.1 and long_diff <= 0.1:
                    return idx
            return None

        usgs_df['sage_idx'] = usgs_df.apply(is_same_event, axis=1)

        # Outer join the dataframes
        merged_df = pd.merge(usgs_df, sage_df, left_on='sage_idx', right_index=True, how='outer')

        # Extract datetime components
        merged_df['year'] = merged_df['time'].dt.year.fillna(merged_df['Time'].dt.year)
        merged_df['month'] = merged_df['time'].dt.month.fillna(merged_df['Time'].dt.month)
        merged_df['day'] = merged_df['time'].dt.day.fillna(merged_df['Time'].dt.day)
        merged_df['hour'] = merged_df['time'].dt.hour.fillna(merged_df['Time'].dt.hour)
        merged_df['min'] = merged_df['time'].dt.minute.fillna(merged_df['Time'].dt.minute)
        merged_df['sec'] = merged_df['time'].dt.second.fillna(merged_df['Time'].dt.second)
        merged_df['ms'] = merged_df['time'].dt.microsecond.fillna(merged_df['Time'].dt.microsecond) / 1000  # Convert to milliseconds

        # Arrange columns
        final_df = merged_df[['year', 'month', 'day', 'hour', 'min', 'sec', 'ms', 'latitude', 'longitude', 'depth', 'mag', 'magType', 'nst', 'gap', 'dmin', 'rms', 'net', 'id', 'horizontalError', 'depthError', 'magError', 'magNst', 'nst']]

        final_df.to_csv('merged_data.csv', index=False)
    def wiki_cleaning_1(self):
        # load the csv file to a pd dataframe
        main = pd.read_csv(self.source[0])

        # manual search of depth of each earthquake (from Wikipedia as well)
        # the mean of the bounds of the interval was used for ranges (e.g. 4.5 km for 4-5 km)
        depth_data_upto17th = np.array([np.nan, 
                                        np.nan,
                                        np.nan,
                                        np.nan,
                                        np.nan,
                                        np.nan,
                                        np.nan,
                                        np.nan,
                                        5.5,
                                        np.nan,
                                        np.nan,
                                        np.nan,
                                        np.nan,
                                        np.nan,
                                        np.nan,
                                        np.nan,
                                        np.nan,
                                        np.nan,
                                        np.nan,
                                        np.nan,
                                        np.nan,
                                        np.nan,
                                        np.nan,
                                        np.nan,
                                        np.nan,
                                        np.nan,
                                        np.nan,
                                        np.nan,
                                        np.nan,
                                        np.nan,
                                        np.nan,
                                        np.nan,
                                        19.5,
                                        np.nan,
                                        np.nan,
                                        np.nan,
                                        np.nan,
                                        np.nan,
                                        np.nan,
                                        np.nan,
                                        np.nan,
                                        np.nan,
                                        np.nan,
                                        np.nan,
                                        np.nan,
                                        np.nan,
                                        np.nan,
                                        27.5,
                                        np.nan,
                                        18.5,
                                        np.nan,
                                        np.nan,
                                        np.nan,
                                        np.nan,
                                        np.nan,
                                        np.nan,
                                        np.nan,
                                        np.nan,
                                        np.nan,
                                        np.nan,
                                        30,
                                        np.nan,
                                        np.nan,
                                        15,
                                        np.nan,
                                        15,
                                        np.nan,
                                        11,
                                        np.nan,
                                        12,
                                        25,
                                        np.nan,
                                        40,
                                        np.nan,
                                        np.nan,
                                        30,
                                        10,
                                        np.nan,
                                        np.nan,
                                        np.nan,
                                        100
                                        ])

        depth_data_18th = np.array([np.nan,
                                    np.nan,
                                    np.nan,
                                    np.nan,
                                    7.5,
                                    np.nan,
                                    np.nan,
                                    np.nan,
                                    np.nan,
                                    np.nan,
                                    np.nan,
                                    np.nan,
                                    np.nan,
                                    40,
                                    30,
                                    np.nan,
                                    np.nan,
                                    np.nan,
                                    np.nan,
                                    np.nan,
                                    np.nan,
                                    np.nan,
                                    np.nan,
                                    15,
                                    np.nan,
                                    85,
                                    10,
                                    np.nan,
                                    20,
                                    np.nan,
                                    20,
                                    np.nan,
                                    np.nan,
                                    np.nan])

        depth_data_19th = np.array([150,
                                    90,
                                    np.nan,
                                    np.nan,
                                    np.nan,
                                    33,
                                    np.nan,
                                    np.nan,
                                    np.nan,
                                    np.nan,
                                    np.nan,
                                    np.nan,
                                    np.nan,
                                    np.nan,
                                    np.nan,
                                    33,
                                    np.nan,
                                    np.nan,
                                    np.nan,
                                    np.nan,
                                    185,
                                    np.nan,
                                    np.nan,
                                    33,
                                    np.nan,
                                    80.5,
                                    10,
                                    np.nan,
                                    np.nan,
                                    30,
                                    np.nan,
                                    np.nan,
                                    80,
                                    30,
                                    10,
                                    9,
                                    np.nan,
                                    np.nan,
                                    np.nan,
                                    np.nan,
                                    60,
                                    np.nan,
                                    np.nan,
                                    np.nan,
                                    np.nan,
                                    np.nan,
                                    np.nan,
                                    np.nan,
                                    np.nan,
                                    np.nan,
                                    12,
                                    np.nan,
                                    10,
                                    np.nan,
                                    np.nan,
                                    np.nan,
                                    np.nan,
                                    np.nan,
                                    34,
                                    np.nan,
                                    np.nan,
                                    np.nan,
                                    np.nan,
                                    np.nan,
                                    15
                                    ])

        # merge all datasets
        depth_data = np.concatenate((depth_data_upto17th,depth_data_18th, depth_data_19th))

        # check if locations match with added depths as it is done manually
        '''
        indices = np.where(depth_data > 0)[0]
        indices = indices.tolist()
        for i in indices:
            print(main.iloc[i])
        '''

        # add depth column to the dataframe
        main['Depth'] = depth_data 

        # print(main)

        # export csv file
        main.to_csv('WikipediaEarthquakes2.csv', index=False)
    def wiki_cleaning_2(self):
        def convert_to_standard_datetime(input_date):
            try:
                # Check if the date has a day component
                date_object = datetime.strptime(input_date, '%Y-%m-%d %H:%M:%S')
                # if input_date.count('-') == 2:
                #     # Try parsing the date with the known format
                #     date_object = datetime.strptime(input_date, '%Y-%m-%d %H:%M:%S')
                # else:
                #     # Stays the same (these entries were manually converted)
                #     return input_date
            except ValueError:
                try:
                    # Try parsing with dateutil.parser for other formats
                    date_object = parser.parse(input_date)
                except ValueError:
                    # Handle the case where the input date is not in a recognizable format
                    return "Invalid Date"

            # Format the date object in a standard datetime format
            standard_format = date_object.strftime('%Y-%m-%d %H:%M:%S.%f+00:00')
            

            return standard_format
        # Read the CSV file into a Pandas DataFrame
        input_file = 'WikipediaEarthquakes2.csv'  # Replace with the actual file path
        output_file = 'WikipediaEarthquakes3.csv'    # Replace with the desired output file path

        df = pd.read_csv(input_file)

        # Remove the BC entries
        df = df.iloc[7:].reset_index(drop=True)

        # Apply the conversion function to the "DateTime" column
        df['DateTime'] = df['DateTime'].apply(convert_to_standard_datetime)

        print(df['DateTime'])

        # print(convert_to_standard_datetime(df['DateTime'][0]))

        # Save the results to a new CSV file
        df.to_csv(output_file, index=False)

        print(f"Conversion completed. Results saved to {output_file}")