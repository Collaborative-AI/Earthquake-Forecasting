from csv import writer
import sys
from pathlib import Path

# Add the parent directory to sys.path
parent_dir = str(Path(__file__).resolve().parent.parent)
sys.path.append(parent_dir)

# import module
from Superclass import Scraper

#canada
class canada(Scraper):
    def __init__(self, input_path, output_path, header,separator):
        self.input_path = input_path
        self.output_path = output_path
        self.header = header    
        self.separator = separator
canada=canada("Canada/Canada-19850109-20230621.txt", "Canada/Canada-19850109-20230621.csv", '','|')
if __name__ == "__main__":
    canada.find_quakes_txt()