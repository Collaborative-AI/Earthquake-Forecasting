# import helper functions for data cleaning
import sys
sys.path.append("src/scraper")

# run on python 3.11.2
import os
from csv import writer
import pandas as pd

from pathlib import Path
parent_dir = str(Path(__file__).resolve().parent.parent)
sys.path.append(parent_dir)
from scraper.Scraper import Scraper
from tqdm import tqdm

class WorldTremor(Scraper):
    def __init__(self, raw_folder="", output_path=""):
        self.raw_folder = raw_folder
        self.output_path = output_path
        
    def find_quakes(self):
        
        # combine all the CSV input files into one output file, as they all have the same schema
        with open(self.output_path, "w") as out_file:
            
            # label the header of the csv with the appropriate labels
            csv_writer = writer(out_file, lineterminator="\n")
            header = ["Date", "Time", "Latitude", "Longitude", "Depth", "Mw", "Source Duration",
                      "Residual Error", "Optional"]
            csv_writer.writerow(header)
            
            # find all csv files from the raw folder
            csv_files = [f for f in os.listdir(self.raw_folder)]
            
            for input_filename in csv_files:
                
                # find the file name through the filepath
                input_path = f"{self.raw_folder}/{input_filename}"
                
                # write each row from the txt file to the csv
                with open(input_path, "r") as input_file:
                    for line in tqdm(input_file):
                        line = line[:-2]
                        row = line.split(",")
                        csv_writer.writerow(row)
            