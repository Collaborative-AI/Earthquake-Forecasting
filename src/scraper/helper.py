import pandas as pd
import numpy as np

"""
INPUT:  filepath to a CSV (string)
OUTPUT: modified CSV that formats timestamps, removes unknown
        magnitudes and coordinates, and drops duplicates
"""
def clean_data(filepath: str):

    # read the csv and read all the columns
    df = pd.read_csv(filepath)
    
    # reformat times, and remove unknown magnitudes + coordinates
    df = replace_with_timestamp(df)
    df = remove_unknown_magnitudes(df)
    df = remove_unknown_coordinates(df)

    # drop duplicates from the dataframe
    df = df.drop_duplicates()

    # store the result in a CSV
    df.to_csv(filepath, index=False)


"""
INPUT:  Pandas DataFrame object (without Timestamp variables)
OUTPUT: Pandas DataFrame object with pd.Timestamp object
"""
def replace_with_timestamp(input_df, tz="UTC"):

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
                                      nanosecond=millisecond*1000, tz=tz)
            
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
def remove_unknown_magnitudes(input_df):

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
def remove_unknown_coordinates(input_df):

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
INPUT:  Row with Schema ["Timestamp", "Magnitude", "Latitude", "Longitude", "Depth"]
OUTPUT: Rounded Timestamp (to 10 seconds), and Magnitude, Latitude and Longitude
        to 1 decimal place
"""
def round_row(input_row):
    timestamp = input_row["Timestamp"]

    # round the seconds to the nearest tens
    rtime = timestamp[-1] + "0"

    # round the magnitude, latitude, and longitude to the nearest tenths place
    rmag = int(10*input_row["Magnitude"])/10
    rlat = int(10*input_row["Latitude"])/10
    rlon = int(10*input_row["Longitude"])/10

    # return the rounded time, mag, lat, and long values to filter out duplicates
    return (rtime, rmag, rlat, rlon)
