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

class New_Madrid_Scraper(Scraper):
    def __init__(self, input_path, output_path, header):
        self.input_path=input_path
        self.output_path=output_path
        self.header=header
if __name__ == "__main__":
    input_path = "New Madrid/New Madrid Earthquakes 1974-2023.txt"
    output_path = "New Madrid/New Madrid Earthquakes 1974-2023.csv"
    header=['NET', 'DATE', 'O.T. (UTC)', 'LAT', 'LONG', 'DEP', \
                      'MAG', 'NPH', 'GAP', 'DMIN', 'RMS', 'SEO', 'SEH', 'SEZ',
                      'Q', 'COMMENTS']
    obj=New_Madrid_Scraper(input_path, output_path, header)
    obj.find_quakes_txt()