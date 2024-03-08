# import helper functions for data cleaning
import sys
sys.path.append("src/scraper")

# run on python 3.11.2
from csv import writer
import pandas as pd

from bs4 import BeautifulSoup
import requests
import io
from datetime import datetime, timedelta
import tabula
import sys
from pathlib import Path
# Add the parent directory to sys.path
parent_dir = str(Path(__file__).resolve().parent.parent)
sys.path.append(parent_dir)

# Now you can import your module
from scraper.Scraper import Scraper
class SouthAsia_Scraper(Scraper):
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
                        
                        # find the time information from the csv
                        year = row[0]
                        month = row[1]
                        day = row[2]
                        hour = row[3]
                        minute = row[4]
                        second = row[5]
                        
                        # although milliseconds aren't present in this csv, 
                        # set the variable to 0 for consistency with other datasets
                        millisecond = 0

                        # find the other rows with data
                        magnitude = row[9]
                        latitude = row[6]
                        longitude = row[7]
                        depth = row[8]

                        # reformat the line
                        output_row = [year, month, day, hour, minute, second, millisecond,
                                    magnitude, latitude, longitude, depth]
                        csv_writer.writerow(output_row)
                    
                    except Exception as e:
                        print(str(e))