import pandas as pd
import requests
import io
from datetime import datetime, timedelta
import random
import time

# Download USGS Data
# Takes 12 hours to run
def download_data(start_date, end_date):
    # USGS request format 
    base_url = "https://earthquake.usgs.gov/fdsnws/event/1/query"

    data = pd.DataFrame()  

    #limit time frame to scraper
    while start_date < end_date:
        # each request consists of 30days of data 
        next_date = start_date + timedelta(days=30)
        if next_date > end_date:
            next_date = end_date

        # parameters used to create the correct request url
        parameters = {
            "format": "csv",
            "starttime": start_date.strftime("%Y-%m-%d"),
            "endtime": next_date.strftime("%Y-%m-%d")
        }

        # make request using the created url
        response = requests.get(base_url, params=parameters)
        response.raise_for_status() 

        csv_data = pd.read_csv(io.StringIO(response.text))
        data = pd.concat([data, csv_data])
        
        start_date = next_date

        # Sleep for a random interval between 3 to 5 minutes
        time_to_sleep = random.randint(180, 300)  # Random time between 180 and 300 seconds
        print(f"Sleeping for {time_to_sleep} seconds")
        time.sleep(time_to_sleep)

    return data

# Start and end dates
start_date = datetime(1800, 1, 1)
end_date = datetime(2023, 6, 12)

# Download data
earthquake_data = download_data(start_date, end_date)

# Save to CSV
earthquake_data.to_csv("/mnt/data/earthquake_data.csv", index=False)
