# import helper functions for data cleaning
import sys
sys.path.append("src/scraper")
from helper import clean_data
import os

# run on python 3.11.2
from csv import writer
import pandas as pd

# converts a txt file (separated by whitespace) to a csv file
def find_quakes(raw_folder: str, output_path: str):
    
    # combine all the CSV input files into one output file, as they all have the same schema
    with open(output_path, "w") as out_file:
        
        # label the header of the csv with the appropriate labels
        csv_writer = writer(out_file, lineterminator="\n")
        header = ["Year/Month/Day", "Hour:Minute:Second", "ET", "GT", "Magnitude",
                  "M", "Latitude", "Longitude", "Depth", "Q", "EVID", "NPH", "NGRM"]
        csv_writer.writerow(header)
                    
        # find all catalog files from the raw folder
        # sort in increasing years
        csv_files = [f for f in os.listdir(raw_folder) if f.endswith(".catalog")]
        csv_files.sort()
        
        for input_filename in csv_files:
            
            # find the file name through the filepath (for tracking error messages)
            input_path = f"{raw_folder}/{input_filename}"
            
            with open(input_path, "r") as input_file:
                
                # skip the first 10 lines of documentation as they don't contain useful info
                for i in range(10):
                    next(input_file, None)
                
                # write each row from the txt file to the csv
                line_number = 1
                for line in input_file:
                    row = line[:-2].split()
                    
                    try:
                        if len(row) == len(header):
                            csv_writer.writerow(row)
                    
                    # print any errors if any have occurred
                    except Exception as e:
                        print(f"For {input_filename} at line {line_number}: {str(e)}")
                    
                    # keep track of line numbers
                    line_number += 1

# main method that calls the web scraper function
if __name__ == "__main__":
    
    # find all csv files in the raw folder
    raw_folder = "src/scraper/SoCal/raw/SCEC_DC"
    
    # combine all the non-Japan earthquakes for the World Tremor Database
    output_filename = "Southern California Earthquakes (1932-2024)"
    output_path = f"src/scraper/SoCal/clean/{output_filename}.csv"
    
    find_quakes(raw_folder, output_path)
