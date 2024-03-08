from csv import writer
from bs4 import BeautifulSoup
import requests
import pandas as pd
import io
from datetime import datetime, timedelta
import tabula
import sys
from pathlib import Path
import random
import time


# Add the parent directory to sys.path
parent_dir = str(Path(__file__).resolve().parent.parent)
sys.path.append(parent_dir)


from scraper.Scraper import Scraper

class usgs_scraper(Scraper):
    def __init__(self, url, start_date, end_date):
        self.url=url
        self.start_date=start_date
        self.end_date=end_date
#Download USGS Data
# Takes 12 hours to run
    def download_data(self):
        # USGS request format 
        base_url = "https://earthquake.usgs.gov/fdsnws/event/1/query"

        # Create empty dataframe to store data
        data = pd.DataFrame()  
        #limit time frame to scraper
        while self.start_date < self.end_date:
            # each request consists of 30days of data 
            next_date = self.start_date + timedelta(days=30)
            if next_date > self.end_date:
                next_date = self.end_date
            # parameters used to create the correct request url
            parameters = {
                "format": "csv",
                "starttime": self.start_date.strftime("%Y-%m-%d"),
                "endtime": next_date.strftime("%Y-%m-%d")
            }
            # make request using the created url
            response = requests.get(self.url, params=parameters)
            response.raise_for_status() 

            csv_data = pd.read_csv(io.StringIO(response.text))
            data = pd.concat([data, csv_data])
            
            self.start_date = next_date
            # Sleep for a random interval between 3 to 5 minutes
            time_to_sleep = random.randint(180, 300)  # Random time between 180 and 300 seconds
            print(f"Sleeping for {time_to_sleep} seconds")
            time.sleep(time_to_sleep)
        return data

if __name__ == "__main__":
    url="https://earthquake.usgs.gov/fdsnws/event/1/query"
    start_date=datetime(1800, 1, 1)
    end_date=datetime(2023, 6, 12)
    obj=usgs_scraper(url, start_date, end_date)
    earthquake_data =obj.download_data()
    earthquake_data.to_csv("/mnt/data/earthquake_data.csv", index=False)

