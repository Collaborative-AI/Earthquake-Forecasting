# import helper functions for data cleaning
import sys
sys.path.append("src/scraper")

# run on python 3.11.2
from csv import writer
import pandas as pd

from pathlib import Path
parent_dir = str(Path(__file__).resolve().parent.parent)
sys.path.append(parent_dir)
from scraper.Scraper import Scraper

class TexasScraper(Scraper):
    def __init__(self, input_path, output_path):
        self.input_path=input_path
        self.output_path=output_path

    # converts a txt file (separated by whitespace) to a csv file
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
                    row = line.split(",")

                    try:
                        
                        # convert the date and time into a pd.Timestamp
                        datetime = f"{row[2]} {row[3]}"
                        ts = pd.Timestamp(datetime)
                        
                        # extract time information from the timestamp
                        year = ts.year
                        month = ts.month
                        day = ts.day
                        hour = ts.hour
                        minute = ts.minute
                        second = ts.second
                        millisecond = ts.microsecond // 1000

                        # find the other rows with data
                        # specifically record moment magnitude
                        magnitude = row[5]
                        latitude = row[6]
                        longitude = row[8]
                        
                        # note: MSL = mean sea level
                        # there are depth values relative to ground surface and MSL,
                        # and here, we choose MSL for consistency with other datasets
                        depth = row[10]

                        # reformat the line
                        output_row = [year, month, day, hour, minute, second, millisecond,
                                    magnitude, latitude, longitude, depth]
                        csv_writer.writerow(output_row)
                    
                    except Exception as e:
                        print(str(e))