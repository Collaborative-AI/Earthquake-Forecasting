from csv import writer
import pandas as pd
import numpy as np

class DataProcessor:
    
    """
    With the exception of datetime and tz, all the parameters are NOT time or location values,
    but rather COLUMN INDEXES that tell the user WHERE a certain value is in the CSV.
    
    If a column index isn't found, then it should be set to None.
    
    Exceptions:
    - datetime: List[int] ---> Some datasets have a separate strings for YYYY/MM/DD and HH:MM:SS
    - tz: str             ---> Non-UTC datasets should specify the timezone.
    """
    def __init__(self, datetime=[], year=None, month=None, day=None,
                 hour=None, minute=None, second=None, millisecond=None, global_tz="UTC", local_tz=None,
                 mag=None, mag_type=None, mag_letter=None, lat=None, long=None, depth=None, energy=None,
                 input_path=""):
        
        """
        Date and Time
        
        Earthquake datasets have two key ways of handling time:
        1. Datetime string (e.g., YYYY-MM-DD HH:MM:SS)
        2. Separate time columns (e.g., "Hour" column)
          
        The processor focuses on using the datetime string if readily available.
        If not, then it will create a datetime object using the numerical
        time values.
        """
        
        # Option 1: Datetime string
        self.datetime = datetime
        
        # Option 2: Time columns
        self.year = year
        self.month = month
        self.day = day
        self.hour = hour
        self.minute = minute
        self.second = second
        self.millisecond = millisecond
        
        """
        Time Zones
        
        Not all datasets are in UTC. If a specified tz is provided, it will be used.
        Datasets either have a
            1. "global" timezone where all row entries are in the same timezone
            2. "local" timezone where each row entry has a different timezone
            
        If you initialize global_tz, you shouldn't initialize local_tz
        or vice versa. If both are initialized, however, local_tz overrides
        global_tz when cleaning datasets in process_quakes()
        """
        self.global_tz = global_tz
        self.local_tz = local_tz
        
        """
        Location
        
        The following values specify column indices for where to find
        location data for earthquakes.
        
        If a dataset provides numerous earthquake events with mixed
        magnitude types (e.g., Md, Mw), only select earthquakes with
        Mw magnitude (aka moment magnitude).
        """
        
        self.mag = mag
        self.mag_type = mag_type
        self.mag_letter = mag_letter
        self.lat = lat
        self.long = long
        self.depth = depth
        self.energy = energy
      
    
    def process_quakes(self, input_path: str, output_path: str):
        with open(input_path, "r") as input_file:
            with open(output_path, "w") as out_file:

                # label the header of the csv with the appropriate labels
                csv_writer = writer(out_file, lineterminator="\n")
                header = ["Year", "Month", "Day", "Hour", "Minute", "Second", "Millisecond",
                        "Magnitude", "Latitude", "Longitude", "Depth"]
                csv_writer.writerow(header)
                next(input_file, None)

                # write each row from the txt file to the csv
                for line in input_file:
                    row = line.split(",")

                    try:
                        
                        """
                        Prior to running the code, check if self.mag_type is non-null.
                        If so, then check if the current row features a magnitude value
                        in moment magnitude.
                        
                        Any mag_type that isn't Mw will be skipped for data consistency.
                        """
                        if self.mag_type != None and row[self.mag_type].lower() != self.mag_letter:
                            continue
                        
                        """
                        Sometimes, the magnitude value isn't a float. In that case,
                        skip this row entry.
                        """
                        if row[self.mag] == "NaN":
                            continue
                        
                        """
                        Date and Time
                        
                        Recall there are two ways to find 
                        If the timestamp is provided use it. If not, recreate it.
                        """
                        
                        # Find the datetime string and the time values
                        datetime = ""
                        year = month = day = hour = minute = second = millisecond = 0
                        
                        # Option 1: The datetime string is provided
                        if self.datetime != None:
                            
                            # Find the time zone based on context
                            tz = self.global_tz
                            if self.local_tz:
                                tz = -1 * int(row[self.local_tz])
                            
                            # Create a pandas Timestamp using the datetime string
                            datetime = self.create_datetime_string([row[index] for index in self.datetime])
                            ts = pd.Timestamp(datetime, tz=tz)
                            ts = ts.tz_convert(tz="UTC")
                            
                            # Extract the time values from the given Timestamp
                            year = ts.year
                            month = ts.month
                            day = ts.day
                            hour = ts.hour
                            minute = ts.minute
                            second = ts.second
                            millisecond = ts.microsecond // 1000
                            
                        # Option 2: The time values are in separate columns
                        else:
                            year = row[self.year]
                            month = row[self.month] if self.month else 1
                            day = row[self.day] if self.day else 1
                            hour = row[self.hour] if self.hour else 0
                            minute = row[self.minute] if self.minute else 0
                            second = row[self.second] if self.second else 0
                            millisecond = row[self.millisecond] if self.millisecond else 0
                            
                            # Edge Case:
                            # Some datasets (e.g., Intensity) include both seconds and milliseconds
                            # into the "Second" column. In this case, update the values to reflect
                            # this edge case.
                            if "." in row[self.second]:
                                second, millisecond = row[self.second].split(".")
                            
                        """
                        Location
                        
                        Extract the magnitude, latitude, longitude, and depth values
                        from the row if provided.
                        
                        If the self.energy value isn't non-null, calculate the value
                        using the following formula found at:
                        https://www.usgs.gov/programs/earthquake-hazards/earthquake-magnitude-energy-release-and-shaking-intensity
                        
                        logE = 5.24 + 1.44(Mw), where Mw = moment magnitude
                        """
                        
                        # Extract the magnitude values
                        magnitude = 0
                        if self.energy:
                            energy = float(row[self.energy])
                            magnitude = (np.emath.logn(10, energy)-5.24)/1.44
                        else:
                            magnitude = float(row[self.mag])
                        
                        # Extract the other values as stated
                        # NOTE: Latitude and longitude are required values,
                        #       but Depth values are optional to include
                        latitude = row[self.lat]
                        longitude = row[self.long]
                        depth = row[self.depth] if self.depth else None

                        # Reformat the line
                        output_row = [year, month, day, hour, minute, second, millisecond,
                                    magnitude, latitude, longitude, depth]
                        csv_writer.writerow(output_row)
					
                    except Exception as e:
                        print(str(e))
    
    """
    Helper function for process_quakes
    
    INPUT:  entries: List of strings contain time information
    OUTPUT: formatted string representing datetime information
    """
    def create_datetime_string(self, entries):
        if len(entries) == 6:
            year, month, day, hour, minute, second = entries
            return f"{year}-{month}-{day}T{hour}:{minute}:{second}Z"
        else:
            return " ".join(entries)
    
    
    """
    INPUT:  filepath: string filepath to the input CSV file
            sort:     boolean notifying if the data needs to be sorted
            
    OUTPUT: modified CSV that formats timestamps, removes unknown
            magnitudes and coordinates, and drops duplicates
    """
    def clean_data(self, filepath: str, sort=True, tz="UTC"):

        # read the csv and read all the columns
        df = pd.read_csv(filepath)
        
        # reformat times, and remove unknown magnitudes + coordinates
        df = self.replace_with_timestamp(df, tz=tz)
        df = self.remove_unknown_magnitudes(df)
        df = self.remove_unknown_coordinates(df)

        # drop duplicates from the dataframe
        df = df.drop_duplicates()
        
        # sort the data if it was originally unsorted
        if sort == True:
            df = self.sort_by_timestamp(df)

        # store the result in a CSV
        df.to_csv(filepath, index=False)


    """
    INPUT:  Pandas DataFrame object (without Timestamp variables)
    OUTPUT: Pandas DataFrame object with pd.Timestamp object
    """
    def replace_with_timestamp(self, input_df, tz="UTC"):

        # replace all separate time columns with one pd.Timestamp column
        output_df = []

        # skip the first column, as it containers the header
        for i in range(len(input_df)):
            row = input_df.iloc[i]

            """
            STEP 1:
            Access time columns from the dataset.
            Prerequisite: The dataset must be preprocessed to match these column names.
            """
            year = row["Year"]
            month = row["Month"]
            day = row["Day"]
            hour = row["Hour"]
            minute = row["Minute"]
            second = row["Second"]
            millisecond = row["Millisecond"]

            """
            STEP 2:
            Cast each value from a numpy.float64 to an int.
            Check for nan values, and if an year is unknown, ignore the data point.
            In this implementation, any unknown value is replaced with a 1.
            """
            if np.isnan(year): continue
            year = int(year)
            month = int(month) if not np.isnan(month) else 1
            day = int(day) if not np.isnan(day) else 1
            hour = int(hour) if not np.isnan(hour) else 1
            minute = int(minute) if not np.isnan(minute) else 1
            second = int(second) if not np.isnan(second) else 1
            millisecond = int(millisecond) if not np.isnan(millisecond) else 1
            
            """
            STEP 3:
            Insert new rows into output_df.

            The try block serves to remove any erroneous rows from the table.
            For example, setting hour=24 is an invalid pd.Timestamp object.
            Exception messages are printed for erroneous rows.
            """
            try:
                # pd.Timestamp doesn't have a millisecond attribute, so we'll use nanoseconds
                frame_time = pd.Timestamp(year=year, month=month, day=day,
                                        hour=hour, minute=minute, second=second,
                                        microsecond=millisecond*1000, tz=tz)
                
                # ensure that the resulting timestamp is in UTC
                frame_time = frame_time.tz_convert(tz="UTC")
                
                # edit the string to include the time along with the timezone (UTC)
                # +00:00 = UTC time in ISO 8601 format
                timestamp_string = f"{frame_time.strftime('%Y-%m-%d %H:%M:%S.%f')}+00:00"
                output_df.append([timestamp_string, row["Magnitude"], row["Latitude"], row["Longitude"], row["Depth"]])
            
            except Exception as e:
                print(f"Error Timestamp (mm/dd/yy hh:mm:ss.ms): {month}/{day}/{year} {hour}:{minute}:{second}.{millisecond}")
                print(f"Exception: {e}\n")

        """
        STEP 4:
        Convert the list into a Pandas dataframe, and return the result!
        """
        output_df = pd.DataFrame(output_df, columns=['Timestamp', 'Magnitude', 'Latitude', 'Longitude', 'Depth'])
        return output_df


    """
    INPUT: Pandas DataFrame  (with unknown magnitudes)
    OUTPUT: Pandas DataFrame (every row has non-null magnitude)
    """
    def remove_unknown_magnitudes(self, input_df):

        # remove any rows with a null latitude or longitude value
        output_df = []
        for i in range(len(input_df)):
            row = input_df.iloc[i]

            """
            STEP 1:
            Find the magnitude for each row
            """
            magnitude = row["Magnitude"]

            """
            STEP 2:
            Only keep rows with non-null and non-zero magnitudes
            """
            if not np.isnan(magnitude) and not -0.01 < magnitude < 0.01:
                output_df.append([row["Timestamp"], row["Magnitude"], row["Latitude"], row["Longitude"], row["Depth"]])
                
        """
        STEP 3:
        Convert the list into a Pandas dataframe, and return the result!
        """
        output_df = pd.DataFrame(output_df, columns=['Timestamp', 'Magnitude', 'Latitude', 'Longitude', 'Depth'])
        return output_df


    """
    INPUT:  Pandas DataFrame (with unknown coordinates)
    OUTPUT: Pandas DataFrame (every row has non-null coordinates)
    """
    def remove_unknown_coordinates(self, input_df):

        # remove any rows with a null latitude or longitude value
        output_df = []
        for i in range(len(input_df)):
            row = input_df.iloc[i]

            """
            STEP 1:
            Find the latitude and longitude values
            """
            latitude = row["Latitude"]
            longitude = row["Longitude"]

            """
            STEP 2:
            Only keep rows with non-null longitude and latitude values
            """
            if not np.isnan(latitude) and not np.isnan(longitude):
                output_df.append([row["Timestamp"], row["Magnitude"], row["Latitude"], row["Longitude"], row["Depth"]])
                
        """
        STEP 3:
        Convert the list into a Pandas dataframe, and return the result!
        """
        output_df = pd.DataFrame(output_df, columns=['Timestamp', 'Magnitude', 'Latitude', 'Longitude', 'Depth'])
        return output_df

    """
    INPUT:  Pandas DataFrame (with unsorted rows)
    OUTPUT: Pandas DataFrame (with rows sorted by timestamp)
    """
    def sort_by_timestamp(self, input_df):
        sorted_df = input_df.sort_values(by='Timestamp', ascending=True)
        return sorted_df
