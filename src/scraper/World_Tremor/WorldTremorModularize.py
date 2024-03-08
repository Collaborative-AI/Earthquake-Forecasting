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

class WorldTremor(Scraper):
    def __init__(self, raw_folder, output_path):
        self.raw_folder = raw_folder
        self.output_path = output_path
    def find_quakes(self):
        
        # combine all the CSV input files into one output file, as they all have the same schema
        with open(self.output_path, "w") as out_file:
            
            # label the header of the csv with the appropriate labels
            csv_writer = writer(out_file, lineterminator="\n")
            header = ["Year", "Month", "Day", "Hour", "Minute", "Second", "Millisecond",
                    "Magnitude", "Latitude", "Longitude", "Depth"]
            csv_writer.writerow(header)
            
            # find all csv files from the raw folder
            csv_files = [f for f in os.listdir(self.raw_folder)]
            
            for input_filename in csv_files:
                
                # find the file name through the filepath (for tracking error messages)
                input_path = f"{self.raw_folder}/{input_filename}"
                
                with open(input_path, "r") as input_file:
                    
                    # write each row from the txt file to the csv
                    line_number = 1
                    for line in input_file:
                        row = line.split(",")
                        
                        # the Japan datasets are set to JST (UTC+9), while
                        # the other datasets are set to UTC.
                        tz = "UTC"
                        if "Kyushu" in input_filename or "Nankai" in input_filename:
                            tz = "Japan"
                        
                        try:
                            
                            # convert the date and time into a pd.Timestamp
                            datetime = f"{row[0]} {row[1]}"
                            ts = pd.Timestamp(datetime, tz=tz)
                            ts = ts.tz_convert(tz="UTC")
                            
                            # extract time information from the timestamp
                            year = ts.year
                            month = ts.month
                            day = ts.day
                            hour = ts.hour
                            minute = ts.minute
                            second = ts.second
                            millisecond = ts.microsecond // 1000

                            # find the other rows with data
                            # NOTE: Magnitude is the maximum of various scales
                            # (e.g., MD, ML, Mw, Ms, Mb)
                            magnitude = row[5]
                            latitude = row[2]
                            longitude = row[3]
                            depth = row[4]

                            # reformat the line
                            output_row = [year, month, day, hour, minute, second, millisecond,
                                        magnitude, latitude, longitude, depth]
                            csv_writer.writerow(output_row)
                        
                        # print any errors if any have occurred
                        except Exception as e:
                            print(f"For {input_filename} at line {line_number}: {str(e)}")
                        
                        # keep track of line numbers
                        line_number += 1