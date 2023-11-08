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
        #self.start_time=datetime.MINYEAR
        #self.end_time=datetime.MAXYEAR
        self.header=[]
    def find_quakes_txt(self):
        with open(self.input_path, "r") as input_file:
            with open(self.output_path, "w") as out_file:

                # label the header of the csv with the appropriate labels
                csv_writer = writer(out_file, lineterminator="\n")
                csv_writer.writerow(self.header)
                numCols = len(self.header)

                # write each row from the txt file to the csv
                for line in input_file:
                    words = line.split()
                    if len(words) == len(self.header):
                        csv_writer.writerow(words)
                    elif len(words) > numCols:
                        words = words[:numCols-1] + [" ".join(words[numCols-1:])]
                        csv_writer.writerow(words)
                    else:
                        csv_writer.writerow(words)

#    def download_data_web():

#if __name__ == "__main__":
    #input_path = "scraper/New Madrid/Earthquakes.txt"
    #output_path = "New Madrid Earthquakes 1974-2023.csv"
    #header=['NET', 'DATE', 'O.T. (UTC)', 'LAT', 'LONG', 'DEP', \
    #                  'MAG', 'NPH', 'GAP', 'DMIN', 'RMS', 'SEO', 'SEH', 'SEZ',
    #                  'Q', 'COMMENTS']
    #obj=Scraper()
    #obj.input_path=input_path
    #obj.output_path=output_path
    #obj.header=header
    #obj.find_quakes_txt()