import csv
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
parent_dir = str(Path(__file__).resolve().parent.parent.parent)
sys.path.append(parent_dir)

# Now you can import your module
from scraper.Scraper import Scraper

class wiki_Scraper(Scraper):
    def __init__(self, url, output_path):
        self.url=url
        self.output_path=output_path
    def find_earthquake(self):
        html_text = requests.get(self.url).text
        #print(html_text)
        soup = BeautifulSoup(html_text, 'lxml')

        date = []
        #place = []
        lat = []
        lon = []
        #fatalities = []
        magnitude = []
        #comments = []

        tables = soup.find_all('table') #each table is an element in the set tables
        for table in tables:
            details = table.find_all('td') #finding all cell info in the table using the td tag
            for i in range(len(details)):
                string = details[i].text.replace('\n', '').replace('Mw','').replace('MS','').replace('Ms','').replace('MI','').replace(
                    '\u202f','').replace('\xa0','') #we only need the text inside the tag; removed unnecessary characters
                if string == '' or string == '?' or string == '\u2013':
                    string = None
                
                if (i%9 == 0): date.append(string)
                #if (i%9 == 2): place.append(string)
                if (i%9 == 3): lat.append(string)
                if (i%9 == 4): lon.append(string)
                #if (i%9 == 5): fatalities.append(string)
                if (i%9 == 6): magnitude.append(string)
                #if (i%9 == 7): comments.append(string)

        file_name = self.output_path #title of the .csv file

        with open(file_name, "w", encoding="utf-8") as f:
            f.write = csv.writer(f)
            f.write.writerow(['DateTime', 'Magnitude', 'Latitude', 'Longitude']) #headers of the .csv file
            for i in range(len(lon)):
                f.write.writerow([date[i], magnitude[i], lat[i], lon[i], ])

if __name__ == '__main__':
    obj=wiki_Scraper('https://en.wikipedia.org/wiki/List_of_historical_earthquakes','WikipediaEarthquakes1.csv')
    obj.find_earthquake()