import pandas as pd
import numpy as np

"""
INPUT:  Pandas DataFrame object (without Timestamp variables)
OUTPUT: Pandas DataFrame object with pd.Timestamp object
"""
def replace_with_timestamp(input_df, tz="UTC"):

    # replace all separate time columns with one pd.Timestamp column
    output_df = []

    # skip the first column, as it containers the header
    for i in range(1, len(input_df)):
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
        
        """
        STEP 3:
        Insert new rows into output_df.

        The try block serves to remove any erroneous rows from the table.
        For example, setting hour=24 is an invalid pd.Timestamp object.
        Exception messages are printed for erroneous rows.
        """
        try:
            # for all valid rows, create a pd.Timestamp and add the result to the output_df
            if second == 60: minute += 1; second = 0
            if minute == 60: hour += 1; minute = 0

            frame_time = pd.Timestamp(year=year, month=month, day=day,
                                      hour=hour, minute=minute, second=second, tz=tz)
            frame_time = frame_time.tz_convert(tz="UTC")
            frame_time = frame_time.tz_localize(None)
            output_df.append([frame_time, row["Magnitude"], row["Latitude"], row["Longitude"], row["Depth"]])
        
        except Exception as e:
            print(f"Error Timestamp (mm/dd/yy hh:mm:ss): {month}/{day}/{year} {hour}:{minute}:{second}")
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
    for i in range(1, len(input_df)):
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
    for i in range(1, len(input_df)):
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

