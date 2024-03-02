import csv
from csv import writer
from bs4 import BeautifulSoup
import requests
import pandas as pd
import io
from datetime import datetime, timedelta
import tabula
import sys
import xmltodict
from pathlib import Path
from tabula.io import read_pdf
import os

# Add the parent directory to sys.path
parent_dir = str(Path(__file__).resolve().parent.parent.parent)
sys.path.insert(0, parent_dir)

# Now you can import your module
from scraper.helper import clean_data
from scraper.scraper import Scraper

class Argentina_Scraper(Scraper):
    def __init__(self, input_path, output_path):
        self.input_path=input_path
        self.output_path=output_path
    def find_quakes(self):
        # open the xml file
        with open(self.input_path, "r") as file:
            file_data = file.read()

        # find all 1436 events in the XML file
        data_dict = xmltodict.parse(file_data)
        data_list = data_dict["quakeml"]["eventParameters"]["event"]

        # find key data points for all earthquakes
        n = len(data_list)
        header = ["Year", "Month", "Day", "Hour", "Minute", "Second", "Millisecond",
                        "Magnitude", "Latitude", "Longitude", "Depth"]

        # collect each event's data in rows
        rows = []
        for row in data_list:
            datetime = row["origin"][0]["time"]["value"]
            mag = row["stationMagnitude"][0]["mag"]["value"]
            lat = row["origin"][0]["latitude"]["value"]
            lon = row["origin"][0]["longitude"]["value"]
            dep = row["origin"][0]["depth"]["value"]

            # split the time into different its numerical values
            date, time = datetime.split("T")
            time = time[:8]
            year, month, day = date.split("-")
            hour, minute, second = time.split(":")
            
            # millisecond data is added manually for dataset consistency
            ms = 0

            # add the results to the CSV
            rows.append([year, month, day, hour, minute, second, ms, mag, lat, lon, dep])

        # write the data into the csv file
        with open(self.output_path, "w") as f:
            csv_writer = csv.writer(f, lineterminator="\n")
            csv_writer.writerow(header)
            csv_writer.writerows(rows)

if __name__ == '__main__':
    input_path = "src/scraper/Argentina/raw/clean-catalog.xml"
    
    output_filename = "Argentina Andean Earthquakes (2016-2017)"
    output_path = f"src/scraper/Argentina/clean/{output_filename}.csv"
    
    argentina=Argentina_Scraper(input_path, output_path)
    argentina.find_quakes()
    clean_data(output_path)