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
    # here, we can do some arithmetic magic by instead dividing the total seconds by 10
    # all earthquakes happening within a 10-second window will share the same rtime value
    ts = pd.Timestamp(input_row["Timestamp"])
    base = pd.Timestamp(year=1, month=1, day=1, hour=0, minute=0, second=0)
    timedelta = ts - base
    rtime = int(timedelta.total_seconds() / 10)

    # round the magnitude, latitude, and longitude to the nearest tenths place
    rmag = int(10*input_row["Magnitude"])/10
    rlat = int(10*input_row["Latitude"])/10
    rlon = int(10*input_row["Longitude"])/10

    # return the rounded time, mag, lat, and long values to filter out duplicates
    return (rtime, rmag, rlat, rlon)
