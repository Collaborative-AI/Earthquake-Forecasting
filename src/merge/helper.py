# run on python 3.11.2
import pandas as pd

"""
INPUT:  Row with Schema ["Timestamp", "Magnitude", "Latitude", "Longitude", "Depth"]
OUTPUT: Rounded Timestamp (to 10 seconds), and Magnitude, Latitude and Longitude
        to 1 decimal place
"""
def round_row(input_row):
    CONFIG_TIME = 10
    CONFIG_EPSILON = 10
    
    timestamp = input_row["Timestamp"]

    # round the seconds to the nearest tens
    # here, we can do some arithmetic magic by instead dividing the total seconds by 10
    # all earthquakes happening within a 10-second window will share the same rtime value
    ts = pd.Timestamp(input_row["Timestamp"])
    base = pd.Timestamp(year=1, month=1, day=1, hour=0, minute=0, second=0)
    timedelta = ts - base
    rtime = int(timedelta.total_seconds() / CONFIG_TIME)

    # round the magnitude, latitude, and longitude to the nearest tenths place
    rmag = int(10*input_row["Magnitude"])/CONFIG_EPSILON
    rlat = int(10*input_row["Latitude"])/CONFIG_EPSILON
    rlon = int(10*input_row["Longitude"])/CONFIG_EPSILON

    # return the rounded time, mag, lat, and long values to filter out duplicates
    return (rtime, rmag, rlat, rlon)

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
