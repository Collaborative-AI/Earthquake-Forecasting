# import helper functions for data preprocessing
import sys
sys.path.append("src/merge")
from helper import replace_with_timestamp, remove_unknown_magnitudes, remove_unknown_coordinates

# import pandas for data manipulation
import pandas as pd

def preprocess_emca():
    csv_file = "src/merge/asia/raw/EMCA Central Asia.csv"

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
    df.to_csv("src/merge/asia/input/EMCA Central Asia.csv", index=False)


def preprocess_south_asia():
    csv_file = "src/merge/asia/raw/South Asia Earthquake Database (1900-2014).csv"

    # read the csv and only keep the specified columns
    df = pd.read_csv(csv_file)
    df = df[["Year", "Month", "Day", "Hour", "Minute", "Seccond",
             "Magnitude (Mw)", "Latitude ", "Longitude", "Depth (km)"]]
    df.rename(columns={"Seccond": "Second",
                       "Magnitude (Mw)": "Magnitude",
                       "Latitude ": "Latitude",
                       "Depth (km)": "Depth"}, inplace=True)
    
    # reformat times, and remove unknown magnitudes + coordinates
    df = replace_with_timestamp(df)
    df = remove_unknown_magnitudes(df)
    df = remove_unknown_coordinates(df)

    # drop duplicates from the dataframe
    df = df.drop_duplicates()

    # store the result in a CSV
    df.to_csv("src/merge/asia/input/South Asia Earthquake Database (1900-2014).csv", index=False)


def preprocess_turkey():
    csv_file = "src/merge/asia/raw/Turkey Earthquakes (1915-2021).csv"

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
    df.to_csv("src/merge/asia/input/Turkey Earthquakes (1915-2021).csv", index=False)


# run the pre-processing functions
preprocess_emca()
preprocess_south_asia()
preprocess_turkey()