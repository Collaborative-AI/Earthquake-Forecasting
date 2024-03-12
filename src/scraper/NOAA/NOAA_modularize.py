import sys
# run on python 3.11.2
from pathlib import Path
from csv import writer
# Add the parent directory to sys.path
parent_dir = str(Path(__file__).resolve().parent.parent)
sys.path.append(parent_dir)

# Now you can import your module
from scraper.Scraper import Scraper

class NOAA_Scraper(Scraper):
    def __init__(self, input_path, output_path, header, separator):
        self.input_path=input_path
        self.output_path=output_path
        self.header=header
        self.separator=separator
