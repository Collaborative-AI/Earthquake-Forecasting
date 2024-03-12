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
        self.separator=None
    def find_quakes(self):
        pass
    def find_quakes_txt(self, num_skips=0):
        with open(self.input_path, "r") as input_file:
            with open(self.output_path, "w") as out_file:

                # label the header of the csv with the appropriate labels
                csv_writer = writer(out_file, lineterminator="\n")
                if self.header!='':
                    csv_writer.writerow(self.header)

                for i in range(num_skips): next(input_file, None)
                # write each row from the txt file to the csv
                for line in input_file:
                    line = line.replace("\n", "")
                    if self.separator == None:
                        words = line.split()
                    else:
                        words = line.split(self.separator)
                    
                    # Get rid of all instances of commas to prevent later bugs
                    for i in range(len(words)):
                        words[i] = words[i].replace(",", "")
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