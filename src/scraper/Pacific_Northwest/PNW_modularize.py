import sys
# run on python 3.11.2
from pathlib import Path
from csv import writer
import pandas as pd
import numpy as np
# Add the parent directory to sys.path
parent_dir = str(Path(__file__).resolve().parent.parent)
sys.path.append(parent_dir)

# Now you can import your module
from scraper.Scraper import Scraper

class PNW_Scraper(Scraper):
    def __init__(self, input_path, output_path):
        self.input_path=input_path
        self.output_path=output_path

    def find_quakes(self):
        
        with open(self.input_path, "r") as input_file:
            with open(self.output_path, "w") as out_file:

                # label the header of the csv with the appropriate labels
                csv_writer = writer(out_file, lineterminator="\n")

                # write each row from the txt file to the csv
                for line in input_file:
                    row = line.split(",")
                    csv_writer.writerow(row)
                    