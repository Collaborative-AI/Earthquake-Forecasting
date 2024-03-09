from csv import writer
import sys
from pathlib import Path

# Add the parent directory to sys.path
parent_dir = str(Path(__file__).resolve().parent.parent)
sys.path.append(parent_dir)

# import module
from scraper.Scraper import Scraper

#canada
class canada(Scraper):
    def __init__(self, input_path, output_path, header,separator):
        self.input_path = input_path
        self.output_path = output_path
        self.header = header    
        self.separator = separator
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
                    if self.separator == None:
                        words = line.split()
                    else:
                        words = line.split(self.separator)
                    csv_writer.writerow(words)
canada_obj=canada("Canada/Canada-19850109-20240119.txt", "Canada/Canada-19850109-20230621.csv", '','|')
if __name__ == "__main__":
    canada_obj.find_quakes_txt()