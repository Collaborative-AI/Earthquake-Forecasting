# run on python 3.11.2
import pandas as pd

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
