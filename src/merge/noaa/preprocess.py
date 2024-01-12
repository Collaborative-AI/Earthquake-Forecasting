# import helper functions for data preprocessing
import sys
sys.path.append("src/merge")
from helper import replace_with_timestamp, remove_unknown_magnitudes, remove_unknown_coordinates

# import pandas for data manipulation
import pandas as pd

def preprocess_GHEA():
    csv_file = "src/merge/noaa/raw/GHEA.csv"

    # read the csv and only keep the specified columns
    df = pd.read_csv(csv_file)
    df = df[["Year", "Mo", "Da", "Ho", "Mi", "Se", "M", "Lat", "Lon", "Dep"]]
    df.rename(columns={"Year": "Year",
                             "Mo": "Month",
                             "Da": "Day",
                             "Ho": "Hour",
                             "Mi": "Minute",
                             "Se": "Second",
                             "M": "Magnitude",
                             "Lat": "Latitude",
                             "Lon": "Longitude",
                             "Dep": "Depth"}, inplace=True)
    
    # reformat times, and remove unknown magnitudes + coordinates
    df = replace_with_timestamp(df)
    df = remove_unknown_magnitudes(df)
    df = remove_unknown_coordinates(df)

    # drop duplicates from the dataframe
    df = df.drop_duplicates()

    # store the result in a CSV
    df.to_csv("src/merge/noaa/input/GHEA.csv", index=False)

def preprocess_NCEI():
    csv_file = "src/merge/noaa/raw/NCEI.csv"

    # read the csv and only keep the specified columns
    df = pd.read_csv(csv_file)
    df = df[["Year", "Mo", "Dy", "Hr", "Mn", "Sec", "Mag", "Latitude", "Longitude", "Focal Depth (km)"]]
    df.rename(columns={"Mo": "Month",
                             "Dy": "Day",
                             "Hr": "Hour",
                             "Mn": "Minute",
                             "Sec": "Second",
                             "Mag": "Magnitude",
                             "Focal Depth (km)": "Depth"}, inplace=True)
    
    # reformat times, and remove unknown magnitudes + coordinates
    df = replace_with_timestamp(df)
    df = remove_unknown_magnitudes(df)
    df = remove_unknown_coordinates(df)

    # drop duplicates from the dataframe
    df = df.drop_duplicates()

    # store the result in a CSV
    df.to_csv("src/merge/noaa/input/NCEI.csv", index=False)


def preprocess_NOAA():
    csv_file = "src/merge/noaa/raw/NOAA.csv";

    # read the csv and only keep the specified columns
    df = pd.read_csv(csv_file)
    df = df[["YEAR", "MONTH", "DAY", "HOUR", "MINUTE", "SECOND", "MAGNITUDE", "LATITUDE", "LONGITUDE", "EQ_DEPTH"]]
    df.rename(columns={"YEAR": "Year",
                             "MONTH": "Month",
                             "DAY": "Day",
                             "HOUR": "Hour",
                             "MINUTE": "Minute",
                             "SECOND": "Second",
                             "MAGNITUDE": "Magnitude",
                             "LATITUDE": "Latitude",
                             "LONGITUDE": "Longitude",
                             "EQ_DEPTH": "Depth"}, inplace=True)
    
    # reformat times, and remove unknown magnitudes + coordinates
    df = replace_with_timestamp(df)
    df = remove_unknown_magnitudes(df)
    df = remove_unknown_coordinates(df)

    # drop duplicates from the dataframe
    df = df.drop_duplicates()

    # store the result in a CSV
    df.to_csv("src/merge/noaa/input/NOAA.csv", index=False)

# rune the pre-processing functions
preprocess_GHEA()
preprocess_NCEI()
preprocess_NOAA()