import pandas as pd
import requests
import io
from datetime import datetime, timedelta

def download_data(start_date, end_date):
    print("Hello World 1")
    base_url = "https://earthquake.usgs.gov/fdsnws/event/1/query"

    data = pd.DataFrame()  
    while start_date < end_date:
        next_date = start_date + timedelta(days=30)
        if next_date > end_date:
            next_date = end_date
        
        parameters = {
            "format": "csv",
            "starttime": start_date.strftime("%Y-%m-%d"),
            "endtime": next_date.strftime("%Y-%m-%d")
        }

        response = requests.get(base_url, params=parameters)
        response.raise_for_status() 

        csv_data = pd.read_csv(io.StringIO(response.text))
        data = pd.concat([data, csv_data])
        
        start_date = next_date

    return data

# Start and end dates
start_date = datetime(1800, 1, 1)
end_date = datetime(2023, 6, 12)

# Download data
earthquake_data = download_data(start_date, end_date)

# Save to CSV
earthquake_data.to_csv("earthquake_data.csv", index=False)
