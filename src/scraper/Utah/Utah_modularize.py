# run on python 3.11.2
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

# converts a txt file (separated by whitespace) to a csv file
class Utah_Scraper(Scraper):
    def __init__(self, input_path, output_path, header):
        self.input_path=input_path
        self.output_path=output_path
        self.header=header
        self.separator=' '
    def find_quakes_txt(self):
        with open(self.input_path, "r") as input_file:
            with open(self.output_path, "w") as out_file:

                # label the header of the csv with the appropriate labels
                csv_writer = writer(out_file, lineterminator="\n")
                csv_writer.writerow(self.header)

                # write each row from the txt file to the csv
                for line in input_file:
                    words = line.split()
                    csv_writer.writerow(words)

# main method that calls the web scraper function
if __name__ == "__main__":
    input_path = "Utah/detections.txt"
    output_path = "Utah/Mineral Mountains, Utah 2016-19.csv"
    header = ["Year", "Origin Time (UTC)", "Latitude", "Longitude",
                      "Depth", "Template Event Magnitude", "Detection Magnitude",
                      "Event Template ID", "Detection ID", "Correlation Coefficient"]
    obj=Utah_Scraper(input_path, output_path, header)
    obj.find_quakes_txt()

