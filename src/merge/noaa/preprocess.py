import pandas as pd
import numpy as np

def replace_with_datetime(input_df):

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
            frame_time = pd.Timestamp(year=year, month=month, day=day,
                                      hour=hour, minute=minute, second=second)
            output_df.append([frame_time, row["Magnitude"], row["Longitude"], row["Latitude"], row["Depth"]])
        
        except Exception as e:
            print(f"Error Timestamp (mm/dd/yy hh:mm:ss): {month}/{day}/{year} {hour}:{minute}:{second}")
            print(f"Exception: {e}\n")

    """
    STEP 4:
    Convert the list into a Pandas dataframe, and return the result!
    """
    output_df = pd.DataFrame(output_df, columns=['DateTime', 'Magnitude', 'Longitude', 'Latitude', 'Depth'])
    return output_df


def preprocess_GHEA():
    csv_file = "src/merge/noaa/raw/GHEA.csv";
    input_df = pd.read_csv(csv_file)
    input_df = input_df[["Year", "Mo", "Da", "Ho", "Mi", "Se", "M", "Lon", "Lat", "Dep"]]
    input_df.rename(columns={"Year": "Year",
                             "Mo": "Month",
                             "Da": "Day",
                             "Ho": "Hour",
                             "Mi": "Minute",
                             "Se": "Second",
                             "M": "Magnitude",
                             "Lon": "Longitude",
                             "Lat": "Latitude",
                             "Dep": "Depth"}, inplace=True)
    input_df.drop_duplicates()
    output_df = replace_with_datetime(input_df)
    output_df.to_csv("src/merge/noaa/input/GHEA.csv", index=False)

def preprocess_NCEI():
    csv_file = "src/merge/noaa/raw/NCEI.csv";
    input_df = pd.read_csv(csv_file)
    input_df = input_df[["Year", "Mo", "Dy", "Hr", "Mn", "Sec", "Mag", "Longitude", "Latitude", "Focal Depth (km)"]]
    input_df.rename(columns={"Mo": "Month",
                             "Dy": "Day",
                             "Hr": "Hour",
                             "Mn": "Minute",
                             "Sec": "Second",
                             "Mag": "Magnitude",
                             "Focal Depth (km)": "Depth"}, inplace=True)
    input_df.drop_duplicates()
    output_df = replace_with_datetime(input_df)
    output_df.to_csv("src/merge/noaa/input/NCEI.csv", index=False)


def preprocess_NOAA():
    csv_file = "src/merge/noaa/raw/NOAA.csv";
    input_df = pd.read_csv(csv_file)
    input_df = input_df[["YEAR", "MONTH", "DAY", "HOUR", "MINUTE", "SECOND", "MAGNITUDE", "LONGITUDE", "LATITUDE", "EQ_DEPTH"]]
    input_df.rename(columns={"YEAR": "Year",
                             "MONTH": "Month",
                             "DAY": "Day",
                             "HOUR": "Hour",
                             "MINUTE": "Minute",
                             "SECOND": "Second",
                             "MAGNITUDE": "Magnitude",
                             "LONGITUDE": "Longitude",
                             "LATITUDE": "Latitude",
                             "EQ_DEPTH": "Depth"}, inplace=True)
    input_df.drop_duplicates()
    output_df = replace_with_datetime(input_df)
    output_df.to_csv("src/merge/noaa/input/NOAA.csv", index=False)

# rune the pre-processing functions
preprocess_GHEA()
preprocess_NCEI()
preprocess_NOAA()