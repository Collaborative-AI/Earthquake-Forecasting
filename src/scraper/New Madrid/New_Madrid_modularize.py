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
    def find_quakes(self):
        with open(self.input_path, "r") as input_file:
            with open(self.output_path, "w") as out_file:

                # label the header of the csv with the appropriate labels
                # label abbreviations: http://folkworm.ceri.memphis.edu/catalogs/html/cat_nm_help.html
                csv_writer = writer(out_file, lineterminator="\n")
                numCols = len(self.header)
                csv_writer.writerow(self.header)

                # write each row from the txt file to the csv
                for line in input_file:
                    words = line.split()

                    # the last column -- COMMENTS -- can consist of multiple words
                    # if so, join the comments together with spaces and put them into one cell
                    if len(words) > numCols:
                        words = words[:numCols-1] + [" ".join(words[numCols-1:])]
                    
                    # afterwards, write these words into the next row
                    csv_writer.writerow(words)
if __name__ == "__main__":
    input_path = "New Madrid/New Madrid Earthquakes 1974-2023.txt"
    output_path = "New Madrid/New Madrid Earthquakes 1974-2023.csv"
    header=['NET', 'DATE', 'O.T. (UTC)', 'LAT', 'LONG', 'DEP', \
                      'MAG', 'NPH', 'GAP', 'DMIN', 'RMS', 'SEO', 'SEH', 'SEZ',
                      'Q', 'COMMENTS']
    obj=New_Madrid_Scraper(input_path, output_path, header)
    obj.find_quakes()