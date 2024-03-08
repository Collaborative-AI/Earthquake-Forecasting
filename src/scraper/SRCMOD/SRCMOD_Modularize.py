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

class SRCMOD_Scraper(Scraper):
    def __init__(self, output_path, url, header):
        self.input_path=''
        self.output_path=output_path
        self.url=url
        self.header=header
        
    def find_quakes_web(self):
    
        # access the website using BeatifulSoup and requests
        r = requests.get(self.url)
        soup = BeautifulSoup(r.text, "html.parser")

        # open a new csv file in a new folder (SRCMOD/srcmod.csv) to write data into
        with open(self.output_path, "w", newline="", encoding="utf8") as f:

            # the header labels each column for readability
            csv_writer = writer(f)
            csv_writer.writerow(self.header)

            # find the earthquakes stored in the website's table (accessed via html <table> tag)
            # for each row's (<tr>) cell (<td>), add the data into a list then append it into the CSV
            quakes = soup.find("table")
            rows = quakes.find_all("tr")
            for row in rows:
                quake_data = []
                for cell in row.find_all("td"):
                    quake_data.append(cell.text.strip())
                csv_writer.writerow(quake_data)
if __name__ == "__main__":
    output_path="SRCMOD/srcmod.csv"
    url="http://equake-rc.info/SRCMOD/searchmodels/allevents/"
    header=["Earthquake ID", "Region", "Date (dd/mm/yyyy)", "Filnn-Engdahl Region", \
                " ", "Magnitude", "Latitude (°N)", "Longitude (°E)", "Depth (km)", \
                "Author", "Upload Date (mm/yyyy)"]
    obj=SRCMOD_Scraper(output_path, url, header)
    obj.find_quakes_web()