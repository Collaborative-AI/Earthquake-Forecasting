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

class Socal_Web_Scraper(Scraper):
    def __init__(self, url, output_path, header):
        self.url=url
        self.output_path=output_path
        self.header=header
if __name__ == "__main__":
    url = "https://service.scedc.caltech.edu/cgi-bin/catalog/catalog_search.pl?outputfmt=scec&start_year=1932&start_month=01&start_day=01&start_hr=00&start_min=00&start_sec=00&end_year=2023&end_month=07&end_day=25&end_hr=00&end_min=00&end_sec=00&min_mag=1&max_mag=9.9&min_depth=0&max_depth=1000.0&south_latd=30.0&north_latd=39.0&west_long=-124.0&east_long=-111.0&etype=eq&gtype=l&file_out=N"
    output_path = "SoCal/Southern California Earthquakes From Web (1932-2023).csv"
    header=["Year/Month/Day", "Hour:Minute:Second", "ET", "GT",
                  "Magnitude", "M", "Latitude", "Longitude", "Depth",
                  "Q", "EVID", "NPH", "NGRM"]
    obj=Socal_Web_Scraper(url, output_path, header)
    obj.find_quakes_web()