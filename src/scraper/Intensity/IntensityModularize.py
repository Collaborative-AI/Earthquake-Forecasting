# import helper functions for data cleaning
import sys
sys.path.append("src/scraper")

# run on python 3.11.2
import os
from csv import writer
import pandas as pd

from pathlib import Path
parent_dir = str(Path(__file__).resolve().parent.parent)
sys.path.append(parent_dir)
from scraper.Scraper import Scraper

class Intensity(Scraper):
    def __init__(self, input_path, output_path):
        self.input_path = input_path
        self.output_path = output_path

    def find_quakes(self):
        
        with open(self.input_path, "r") as input_file:
            with open(self.output_path, "w") as out_file:

                # label the header of the csv with the appropriate labels
                csv_writer = writer(out_file, lineterminator="\n")
                header = ["Year", "Month", "Day", "Hour", "Minute", "Second", "Millisecond",
                        "Magnitude", "Latitude", "Longitude", "Depth"]
                csv_writer.writerow(header)
                next(input_file, None)

                # write each row from the txt file to the csv
                for line in input_file:
                    
                    try:
                        row = line.split(",")
                        
                        # find the time data
                        local_year = int(row[0])
                        local_month = int(row[1]) if row[1] else 1
                        local_day = int(row[2]) if row[2] else 1
                        local_hour = int(row[3]) if row[3] else 0
                        local_minute = int(row[4]) if row[4] else 0
                        
                        # seconds are formatted poorly in the input csv
                        local_second = local_millisecond = 0
                        
                        # if row[5] is a float (e.g., 44.6), then extract
                        # the second and millisecond value
                        if "." in row[5]:
                            total_milliseconds = int(float(row[5]) * 1000)
                            local_second, local_millisecond = divmod(total_milliseconds, 1000)
                        
                        # if row[5] is an int, then extract only the second
                        # if row[5] is neither an int or a float, do nothing
                        elif row[5]:
                            local_second = int(row[5])
                        
                        # find the timezone offset (LOCAL_TO_UTC)
                        tz_offset = -1 * int(row[6]) if row[6] else 0
                        
                        # the earthquakes in this dataset feature local times
                        # so we'll update the values to UTC
                        ts = pd.Timestamp(year=local_year, month=local_month, day=local_day,
                                        hour=local_hour, minute=local_minute, second=local_second,
                                        microsecond = local_millisecond*1000, tz=tz_offset)
                        ts = ts.tz_convert(tz="UTC")
                        
                        # find the updated time values
                        year = ts.year
                        month = ts.month
                        day = ts.day
                        hour = ts.hour
                        minute = ts.minute
                        second = ts.second
                        millisecond = ts.microsecond // 1000
                        
                        # find other earthquake attribute data
                        magnitude = row[10]
                        latitude = row[8]
                        longitude = row[9]
                        depth = row[11]
                        
                        # add the output row to the csv
                        output_row = [year, month, day, hour, minute, second, millisecond,
                                        magnitude, latitude, longitude, depth]
                        csv_writer.writerow(output_row)
                        
                    except Exception as e:
                        print(str(e))
                        break