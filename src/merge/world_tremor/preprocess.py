# import helper functions for data preprocessing
import sys
sys.path.append("src/merge")
from helper import replace_with_timestamp, remove_unknown_magnitudes, remove_unknown_coordinates

# import pandas for data manipulation
import pandas as pd

def preprocess_kyushu():
    csv_file = "src/merge/world_tremor/raw/Kyushu-20040401-20130331.csv"

    # read the csv and only keep the specified columns
    df = pd.read_csv(csv_file, names =["Year", "Month", "Day", "Hour", "Minute", "Second",
                                         "Magnitude", "Latitude", "Longitude", "Depth"])
    
    # reformat times, and remove unknown magnitudes + coordinates
    df = replace_with_timestamp(df, tz="Asia/Tokyo")
    df = remove_unknown_magnitudes(df)
    df = remove_unknown_coordinates(df)

    # drop duplicates from the dataframe
    df = df.drop_duplicates()

    # store the result in a CSV
    df.to_csv("src/merge/world_tremor/input/Kyushu-20040401-20130331.csv", index=False)


def preprocess_nankai():
    csv_file = "src/merge/world_tremor/raw/Nankai-20040401-20130329.csv"

    # read the csv and only keep the specified columns
    df = pd.read_csv(csv_file, names =["Year", "Month", "Day", "Hour", "Minute", "Second",
                                         "Magnitude", "Latitude", "Longitude", "Depth"])
    
    # reformat times, and remove unknown magnitudes + coordinates
    df = replace_with_timestamp(df, tz="Asia/Tokyo")
    df = remove_unknown_magnitudes(df)
    df = remove_unknown_coordinates(df)

    # drop duplicates from the dataframe
    df = df.drop_duplicates()

    # store the result in a CSV
    df.to_csv("src/merge/world_tremor/input/Nankai-20040401-20130329.csv", index=False)


# run the pre-processing functions
preprocess_kyushu()
preprocess_nankai()