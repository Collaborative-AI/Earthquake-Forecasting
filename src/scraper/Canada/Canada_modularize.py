# import helper functions for data cleaning
import sys
sys.path.append("src/scraper")
from helper import clean_data

# run on python 3.11.2
from csv import writer
import pandas as pd
from pathlib import Path


parent_dir = str(Path(__file__).resolve().parent.parent.parent)
sys.path.insert(0, parent_dir)

# Now you can import your module
from scraper.helper import clean_data
from scraper.scraper import Scraper

class Canada_Scraper(Scraper):
    def __init__(self, input_path, output_path):
        self.input_path=input_path
        self.output_path=output_path
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
                    row = line.split("|")
                    
                    # if the magtype isn't "mw", ignore the result
                    if row[5].lower() != "mw":
                        continue
                    
                    # extract the date and time as a pd.Timestamp object
                    ts = pd.Timestamp(row[1])
                    
                    # extract the attributes from the pd.Timestamp object
                    year = ts.year
                    month = ts.month
                    day = ts.day
                    hour = ts.hour
                    minute = ts.minute
                    second = ts.second
                    millisecond = ts.microsecond // 1000
                    
                    # access the other attributes in the row
                    magnitude = row[6]
                    latitude = row[2]
                    longitude = row[3]
                    depth = row[4]

                    # update the row with the new date and time columns
                    output_row = [year, month, day, hour, minute, second, millisecond,
                                magnitude, latitude, longitude, depth]
                    csv_writer.writerow(output_row)

# main method that calls the web scraper function
if __name__ == "__main__":
    input_path = "src/scraper/Canada/raw/Canada-19850109-20240117.txt"
    
    output_filename = "Canada (1985-2024)"
    output_path = f"src/scraper/Canada/clean/{output_filename}.csv"
    
    Canada = Canada_Scraper(input_path, output_path)
    Canada.find_quakes()
    clean_data(output_path)
