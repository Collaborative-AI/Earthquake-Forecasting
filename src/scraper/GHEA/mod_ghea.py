from csv import writer
import sys
from pathlib import Path

# Add the parent directory to sys.path
parent_dir = str(Path(__file__).resolve().parent.parent)
sys.path.append(parent_dir)

# import module
from Superclass import Scraper


# converts a txt file (separated by whitespace) to a csv file
class GHEA(Scraper):
    def __init__(self, input_path, output_path, header,separator):
        self.input_path = input_path
        self.output_path = output_path
        self.header = header    
        self.separator = separator
                    
ghea=GHEA("GHEA/GHEA-data.txt", "GHEA/GHEA Data 1000-1903.csv", ["En", "Source", "Year", "Mo", "Da", "Ho", "Mi", "Se",
                          "Area", "Lat", "Lon", "LatUnc", "LonUnc", "EpDet", "Dep",
                          "Io", "Msource", "M", "MUnc", "MType", "MDet", "MDPSource",
                          "MDPn", "MDPIx", "MDPsc", "Remarks", "GEHid"],"\t")
if __name__ == "__main__":
    ghea.find_quakes_txt()
