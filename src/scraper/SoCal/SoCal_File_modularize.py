from csv import writer
from bs4 import BeautifulSoup
import requests
import pandas as pd
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

class Socal_File_Scraper(Scraper):
    def __init__(self, input_path, output_path, header):
        self.input_path=input_path
        self.output_path=output_path
        self.header=header
        self.separator=None
    def find_quakes_txt(self, num_skips=0):
        with open(self.input_path, "r") as input_file:
            with open(self.output_path, "w") as out_file:

                # label the header of the csv with the appropriate labels
                csv_writer = writer(out_file, lineterminator="\n")
                if self.header!='':
                    csv_writer.writerow(self.header)

                for i in range(num_skips): next(input_file, None)
                # write each row from the txt file to the csv
                for line in input_file:
                    if self.separator == None:
                        words = line.split()
                    else:
                        words = line.split(self.separator)
                    csv_writer.writerow(words)
if __name__ == "__main__":
    input_path = "SoCal/SearchResults.txt"
    output_path = "SoCal/Southern California Earthquakes (1932-2023).csv"
    header=["Year/Month/Day", "Hour:Minute:Second", "ET", "GT",
                      "Magnitude", "M", "Latitude", "Longitude", "Depth",
                      "Q", "EVID", "NPH", "NGRM"]
    obj=Socal_File_Scraper(input_path, output_path, header)
    obj.find_quakes_txt(3)