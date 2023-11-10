from csv import writer
from bs4 import BeautifulSoup
import requests
import pandas as pd
import io
from datetime import datetime, timedelta
import tabula

class Scraper:
    def __init__(self):
        self.input_path=''
        self.output_path=''
        self.url=''
        self.start_time=datetime.MINYEAR
        self.end_time=datetime.MAXYEAR
        self.header=[]
        self.separator=''
    def find_quakes_txt(self):
        with open(self.input_path, "r") as input_file:
            with open(self.output_path, "w") as out_file:

                # label the header of the csv with the appropriate labels
                csv_writer = writer(out_file, lineterminator="\n")
                csv_writer.writerow(self.header)

                # write each row from the txt file to the csv
                for line in input_file:
                    words = line.split(self.separator)
                    csv_writer.writerow(words)

    def find_quakes_web(self):
    
        # access the website using BeatifulSoup and requests
        r = requests.get(self.url)
        soup = BeautifulSoup(r.text, "html.parser")

        # open a new csv file in the output path to write data into
        with open(self.output_path, "w", newline="", encoding="utf8") as f:

            # the header labels each column for readability
            csv_writer = writer(f, lineterminator="\n")
            # csv_writer.writerow(header)

            # find the earthquakes stored in the website's table (accessed via html <body> tag)
            quakes = soup.find("body").text
            rows = quakes.split("\n")

            # only add rows with earthquake data by checking its length with the header
            for row in rows:
                data = row.split()
                if len(data) == len(self.header):
                    csv_writer.writerow(data)