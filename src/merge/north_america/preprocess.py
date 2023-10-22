# import helper functions for data preprocessing
import sys
sys.path.append("src/merge")
from helper import replace_with_timestamp, remove_unknown_magnitudes, remove_unknown_coordinates

# import pandas for data manipulation
import pandas as pd

def preprocess_canada():
    csv_file = "src/merge/north_america/raw/Canada-19850109-20230621.csv"

    # read the csv and only keep the specified columns
    df = pd.read_csv(csv_file)
    df = df[["Year", "Month", "Day", "Hour", "Minute", "Second",
             "Magnitude", "Latitude", "Longitude", "Depth/km"]]
    df.rename(columns={"Depth/km": "Depth"}, inplace=True)
    
    # reformat times, and remove unknown magnitudes + coordinates
    df = replace_with_timestamp(df)
    df = remove_unknown_magnitudes(df)
    df = remove_unknown_coordinates(df)

    # drop duplicates from the dataframe
    df = df.drop_duplicates()

    # store the result in a CSV
    df.to_csv("src/merge/north_america/input/Canada-19850109-20230621.csv", index=False)


def preprocess_mexico():
    csv_file = "src/merge/north_america/raw/Mexico Earthquake Catalog (1787-2018).csv"

    # read the csv and only keep the specified columns
    df = pd.read_csv(csv_file)
    df = df[["Year", "Month", "Day", "Hour", "Minute", "Second",
             "Mw", "Latitude", "Longitude", "Depth"]]
    df.rename(columns={"Mw": "Magnitude"}, inplace=True)
    
    # reformat times, and remove unknown magnitudes + coordinates
    df = replace_with_timestamp(df)
    df = remove_unknown_magnitudes(df)
    df = remove_unknown_coordinates(df)

    # drop duplicates from the dataframe
    df = df.drop_duplicates()

    # store the result in a CSV
    df.to_csv("src/merge/north_america/input/Mexico Earthquake Catalog (1787-2018).csv", index=False)


def preprocess_mineral_mountains():
    csv_file = "src/merge/north_america/raw/Mineral Mountains, Utah 2016-19.csv"

    # read the csv and only keep the specified columns
    df = pd.read_csv(csv_file)
    df = df[["Year", "Month", "Day", "Hour", "Minute", "Second",
             "Detection Magnitude", "Latitude", "Longitude", "Depth"]]
    df.rename(columns={"Detection Magnitude": "Magnitude"}, inplace=True)
    
    # reformat times, and remove unknown magnitudes + coordinates
    df = replace_with_timestamp(df)
    df = remove_unknown_magnitudes(df)
    df = remove_unknown_coordinates(df)

    # drop duplicates from the dataframe
    df = df.drop_duplicates()

    # store the result in a CSV
    df.to_csv("src/merge/north_america/input/Mineral Mountains, Utah 2016-19.csv", index=False)


# rune the pre-processing functions
preprocess_canada()
preprocess_mexico()
preprocess_mineral_mountains()