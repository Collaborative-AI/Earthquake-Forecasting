import sys
sys.path.append("src/scraper")
from pathlib import Path
# run on python 3.11.2
from csv import writer
import pandas as pd

parent_dir = str(Path(__file__).resolve().parent.parent)
sys.path.append(parent_dir)
from scraper.Scraper import Scraper

class EastAfrica(Scraper):
    def __init__(self, input_path, output_path, header,separator):
        self.input_path = input_path
        self.output_path = output_path
        self.header = header    
        self.separator = separator


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
                        
                        # check if Mw (moment magnitude) is defined
                        magnitude = row[1]
                        if magnitude == "NaN":
                            continue
                        
                        # put each time unit (excluding ms) in separate columns
                        # IRIS format splits date and time using T
                        ts = pd.Timestamp(row[6])
                        
                        # extract the attributes from the pd.Timestamp object
                        year = ts.year
                        month = ts.month
                        day = ts.day
                        hour = ts.hour
                        minute = ts.minute
                        second = ts.second
                        millisecond = ts.microsecond // 1000

                        # find the other rows with data
                        latitude = row[7]
                        longitude = row[8]
                        depth = row[9]

                        # reformat the line
                        output_row = [year, month, day, hour, minute, second, millisecond,
                                    magnitude, latitude, longitude, depth]
                        csv_writer.writerow(output_row)
                    
                    except Exception as e:
                        print(str(e))