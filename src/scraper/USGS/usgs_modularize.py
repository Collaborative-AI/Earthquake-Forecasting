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
from Superclass import Scraper

class usgs_scraper(Scraper):
    def __init__(self, url, start_date, end_date):
        self.url=url
        self.start_date=start_date
        self.end_date=end_date

    def download_data(self):
        print("Hello World 1")

        data = pd.DataFrame()  
        while self.start_date < self.end_date:
            next_date = self.start_date + timedelta(days=30)
            if next_date > self.end_date:
                next_date = self.end_date
            
            parameters = {
                "format": "csv",
                "starttime": self.start_date.strftime("%Y-%m-%d"),
                "endtime": next_date.strftime("%Y-%m-%d")
            }

            response = requests.get(self.url, params=parameters)
            response.raise_for_status() 

            csv_data = pd.read_csv(io.StringIO(response.text))
            data = pd.concat([data, csv_data])
            
            self.start_date = next_date

        return data

if __name__ == "__main__":
    url="https://earthquake.usgs.gov/fdsnws/event/1/query"
    start_date=datetime(1800, 1, 1)
    end_date=datetime(2023, 6, 12)
    obj=usgs_scraper(url, start_date, end_date)
    earthquake_data =obj.download_data()
    earthquake_data.to_csv("earthquake_data.csv", index=False)
