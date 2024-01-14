# import helper functions for data merging
import sys
sys.path.append("src/merge")

# run on python 3.11.2
from helper import round_row
import pandas as pd

"""
merge.py

This python file merges earthquake catalogs by geographical regions (e.g.,
North America, Asia), then merges the region datasets together into one
worldwide dataset.

The output dataset will be found in the src/merge/ folder, and the
resulting CSV is guaranteed to be:

1. Sorted in chronological order
2. Distinct (aka no duplicates)

"""


"""
merge_group function

INPUT:  csv_files:   List of input paths of earthquake datasets to merge together
        output_path: Filepath for where the output CSV will be generated
OUTPUT: Merged CSV of distinct earthquake events sorted in chronological order
"""
def merge_group(csv_files: list, output_path):
    
    """
    STEP 1:
    Load the data frames.
    The header will be ["Datetime", "Magnitude", "Longitude", "Latitude", "Depth"].
    """
    frames = [pd.read_csv(csv_file) for csv_file in csv_files]
    
    """
    STEP 2:
    Use a hashmap to keep track of duplicate earthquakes
    seen[time] = [magnitude, longitude, latitude]
    """
    seen = dict()
    result = []

    for frame in frames:
        for i in range(1, len(frame)):

            # access the current row
            row = frame.iloc[i]

            # find the rounded time, mag, lat, and long values
            # find helper.py for details about this function
            rtime, rmag, rlat, rlon = round_row(row)

            # if we've never seen this key before, intialize a list
            # this represents all earthquakes at this time
            if rtime not in seen:
                seen[rtime] = []
            
            # if we've seen this earthquake before at this time, it's a duplicate!
            if (rmag, rlat, rlon) in seen[rtime]:
                continue
            
            # otherwise, treat this earthquake as unique
            # append the data into the result
            result.append([row["Timestamp"], row["Magnitude"], row["Latitude"], row["Longitude"], row["Depth"]])
            
    """
    STEP 3:
    Sort the earthquakes in increasing order.
    """
    result.sort(key=lambda x: x[0])
    
    """
    STEP 4:
    Convert the resulting list to a DataFrame and export it.
    
    Algorithmic Analysis:
    n = total number of rows of all input datasets
    
    O(nlogn) time due to sorting
    O(n) extra space for newly-created lists
    """
    result_df = pd.DataFrame(result, columns=['Timestamp', 'Magnitude', 'Latitude', 'Longitude', 'Depth'])
    result_df.to_csv(output_path, index=False)
