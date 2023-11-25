from csv import writer
import sys
from pathlib import Path

# Add the parent directory to sys.path
parent_dir = str(Path(__file__).resolve().parent.parent)
sys.path.append(parent_dir)

# import module
from Superclass import Scraper

#Corinth
class corinth(Scraper):
    def __init__(self, input_path, output_path, header, separator):
        self.input_path = input_path
        self.output_path = output_path
        self.header = header    
        self.separator = separator

corinth = corinth("Corinth/Marathias_seq.txt", "Corinth/Corinth Gulf 2020-21 Seismic Crisis.csv", ["Year", "Origin Time", "Latitude", "Longitude", "Depth",
                      "Magnitude", "Decimal Years", "Time Relative to First Earthquake",
                      "Event ID", "Cluster ID (sorted by #events)",
                      "Cluster ID (by time)", "Multiplet ID", "#events in Multiplet",
                      "E-W horizontal error", "N-S horizontal error",
                      "Vertical error"], None)

if __name__ == "__main__":
    corinth.find_quakes_txt()