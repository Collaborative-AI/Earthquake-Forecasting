# import helper functions for data preprocessing
import sys
sys.path.append("src/merge")
from helper import replace_with_timestamp, remove_unknown_magnitudes, remove_unknown_coordinates

# import pandas for data manipulation
import pandas as pd

def preprocess_argentina():
    csv_file = "src/merge/misc/raw/Argentina Andean Earthquakes (2016-2017).csv"

    # read the csv and only keep the specified columns
    df = pd.read_csv(csv_file)
    df = df[["Year", "Month", "Day", "Hour", "Minute", "Second",
             "Magnitude", "Latitude", "Longitude", "Depth"]]
    
    # reformat times, and remove unknown magnitudes + coordinates
    df = replace_with_timestamp(df)
    df = remove_unknown_magnitudes(df)
    df = remove_unknown_coordinates(df)

    # drop duplicates from the dataframe
    df = df.drop_duplicates()

    # store the result in a CSV
    df.to_csv("src/merge/misc/input/Argentina Andean Earthquakes (2016-2017).csv", index=False)


def preprocess_corinth():
    csv_file = "src/merge/misc/raw/Corinth Gulf 2020-21 Seismic Crisis.csv"

    # read the csv and only keep the specified columns
    df = pd.read_csv(csv_file)
    df = df[["Year", "Month", "Day", "Hour", "Minute", "Second",
             "Magnitude", "Latitude", "Longitude", "Depth"]]
    
    # reformat times, and remove unknown magnitudes + coordinates
    df = replace_with_timestamp(df)
    df = remove_unknown_magnitudes(df)
    df = remove_unknown_coordinates(df)

    # drop duplicates from the dataframe
    df = df.drop_duplicates()

    # store the result in a CSV
    df.to_csv("src/merge/misc/input/Corinth Gulf 2020-21 Seismic Crisis.csv", index=False)


def preprocess_east_africa():
    csv_file = "src/merge/misc/raw/East Africa Rift System (1994-2022).csv"

    # read the csv and only keep the specified columns
    df = pd.read_csv(csv_file)
    df = df[["Year", "Month", "Day", "Hour", "Minute", "Second",
             "Magnitude", "Latitude", "Longitude", "Depth"]]
    
    # reformat times, and remove unknown magnitudes + coordinates
    df = replace_with_timestamp(df)
    df = remove_unknown_magnitudes(df)
    df = remove_unknown_coordinates(df)

    # drop duplicates from the dataframe
    df = df.drop_duplicates()

    # store the result in a CSV
    df.to_csv("src/merge/misc/input/East Africa Rift System (1994-2022).csv", index=False)


# run the pre-processing functions
preprocess_argentina()
preprocess_corinth()
preprocess_east_africa()