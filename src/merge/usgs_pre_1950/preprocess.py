# import helper functions for data preprocessing
import sys
sys.path.append("src/merge")
from helper import replace_with_timestamp, remove_unknown_magnitudes, remove_unknown_coordinates

# import pandas for data manipulation
import pandas as pd

def preprocess_usgs_1800_1849():
    csv_file = "src/merge/usgs_pre_1950/raw/USGS1800-1849.csv"

    # read the csv and only keep the specified columns
    df = pd.read_csv(csv_file)
    df = df[["time", "mag", "latitude", "longitude", "depth"]]
    df.rename(columns={"time": "Timestamp",
                       "mag": "Magnitude",
                       "latitude" : "Latitude",
                       "longitude" : "Longitude",
                       "depth": "Depth"}, inplace=True)
    
    # reformat times, and remove unknown magnitudes + coordinates
    df = remove_unknown_magnitudes(df)
    df = remove_unknown_coordinates(df)

    # drop duplicates from the dataframe
    df = df.drop_duplicates()

    # store the result in a CSV
    df.to_csv("src/merge/usgs_pre_1950/input/USGS1800-1849.csv", index=False)


def preprocess_usgs_1850_1899():
    csv_file = "src/merge/usgs_pre_1950/raw/USGS1850-1899.csv"

    # read the csv and only keep the specified columns
    df = pd.read_csv(csv_file)
    df = df[["time", "mag", "latitude", "longitude", "depth"]]
    df.rename(columns={"time": "Timestamp",
                       "mag": "Magnitude",
                       "latitude" : "Latitude",
                       "longitude" : "Longitude",
                       "depth": "Depth"}, inplace=True)
    
    # reformat times, and remove unknown magnitudes + coordinates
    df = remove_unknown_magnitudes(df)
    df = remove_unknown_coordinates(df)

    # drop duplicates from the dataframe
    df = df.drop_duplicates()

    # store the result in a CSV
    df.to_csv("src/merge/usgs_pre_1950/input/USGS1850-1899.csv", index=False)


def preprocess_usgs_1900_1949():
    csv_file = "src/merge/usgs_pre_1950/raw/USGS1900-1949.csv"

    # read the csv and only keep the specified columns
    df = pd.read_csv(csv_file)
    df = df[["time", "mag", "latitude", "longitude", "depth"]]
    df.rename(columns={"time": "Timestamp",
                       "mag": "Magnitude",
                       "latitude" : "Latitude",
                       "longitude" : "Longitude",
                       "depth": "Depth"}, inplace=True)
    
    # reformat times, and remove unknown magnitudes + coordinates
    df = remove_unknown_magnitudes(df)
    df = remove_unknown_coordinates(df)

    # drop duplicates from the dataframe
    df = df.drop_duplicates()

    # store the result in a CSV
    df.to_csv("src/merge/usgs_pre_1950/input/USGS1900-1949.csv", index=False)


# run the pre-processing functions
preprocess_usgs_1800_1849()
preprocess_usgs_1850_1899()
preprocess_usgs_1900_1949()
