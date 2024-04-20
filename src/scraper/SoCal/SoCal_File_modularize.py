from csv import writer
import os
import sys
from pathlib import Path

# Add the parent directory to sys.path
parent_dir = str(Path(__file__).resolve().parent.parent)
sys.path.append(parent_dir)

# Now you can import your module
from scraper.Scraper import Scraper

class Socal_File_Scraper(Scraper):
    def __init__(self, input_path, output_path, header):
        self.input_path=input_path
        self.output_path=output_path
        self.header=header
        self.separator=None
    def find_quakes(self):
        # combine all the CSV input files into one output file, as they all have the same schema
        with open(self.output_path, "w") as out_file:
            
            # label the header of the csv with the appropriate labels
            csv_writer = writer(out_file, lineterminator="\n")
            header = ["Year/Month/Day", "Hour:Minute:Second", "ET", "GT", "Magnitude",
                    "M", "Latitude", "Longitude", "Depth", "Q", "EVID", "NPH", "NGRM"]
            csv_writer.writerow(header)
                        
            # find all catalog files from the raw folder
            # sort in increasing years
            csv_files = [f for f in os.listdir(self.input_path) if f.endswith(".catalog")]
            csv_files.sort()
            
            for input_filename in csv_files:
                
                # find the file name through the filepath (for tracking error messages)
                input_path = f"{self.input_path}/{input_filename}"
                
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
        
        
if __name__ == "__main__":
    input_path = "SoCal/raw/SCEC_DC"
    output_path = "SoCal/SCEDC (1932-2024).csv"
    header = ["Year/Month/Day", "Hour:Minute:Second", "ET", "GT", "Magnitude",
              "M", "Latitude", "Longitude", "Depth", "Q", "EVID", "NPH", "NGRM"]
    obj=Socal_File_Scraper(input_path, output_path, header)
    obj.find_quakes_txt(3)