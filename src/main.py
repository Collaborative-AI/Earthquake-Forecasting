from scraper import *
from datetime import datetime
from csv import writer
import sys

if __name__ == "__main__":
    
    # Argentina Scraper
    input_path = "src/scraper/Argentina/raw/clean-catalog.xml"
    output_path = "src/scraper/Argentina/clean/Argentina Andean Earthquakes (2016-2017).csv"
    header = ["Time ID", "Magnitude", "Latitude", "Longitude", "Depth"]
    argentina = Argentina(input_path, output_path, header)
    argentina.find_quakes()
    
    # Canada Scraper
    input_path = "src/scraper/Canada/raw/Canada-19850109-20240119.txt"
    output_path = "src/scraper/Canada/clean/Canada (1985-2024).csv"
    separator = '|'
    canada = Scraper(input_path=input_path, output_path=output_path, separator=separator)
    canada.find_quakes_txt(num_skips=0)
    
    # Japan Scraper
    input_path = "src/scraper/World_Tremor/japan"
    output_path = f"src/scraper/World_Tremor/clean/Japan Database (2005-2014).csv"
    obj = WorldTremor(raw_folder=input_path, output_path=output_path)
    obj.find_quakes()
    
    # GHEA Scraper
    input_path = "src/scraper/GHEA/raw/GHEA-data.txt"
    output_path = "src/scraper/GHEA/clean/GHEA (1000-1903).csv"
    separator = "\t"
    ghea = GHEA(input_path=input_path, output_path=output_path, separator=separator)
    ghea.find_quakes_txt(num_skips=78)
    
    # NOAA Scraper
    input_path = "src/scraper/NOAA/raw/NCEI-WDS-Earthquakes.tsv"
    output_path = f"src/scraper/NOAA/clean/NOAA NCEI-WDS (0-2023).csv"
    separator = "\t"
    noaa = Scraper(input_path=input_path, output_path=output_path, separator=separator)
    noaa.find_quakes_txt(num_skips=0)
    
    # SoCal Scraper
    input_path = "src/scraper/SoCal/raw/SearchResults.txt"
    output_path = "src/scraper/SoCal/clean/SCEDC (1932-2023).csv"
    obj = Scraper(input_path=input_path, output_path=output_path)
    obj.find_quakes_txt(num_skips=2)
    
    # Turkey Scraper
    input_path = "src/scraper/Turkey/raw/turkey_earthquakes(1915-2021).csv"
    output_path = "src/scraper/Turkey/clean/Turkey (1915-2021).csv"
    separator = ";"
    obj = Scraper(input_path=input_path, output_path=output_path, separator=separator)
    obj.find_quakes_txt(num_skips=0)
    
    # World Tremor Scraper
    input_path = "src/scraper/World_Tremor/global"
    output_path = f"src/scraper/World_Tremor/clean/World Tremor Database (2005-2014).csv"
    obj = WorldTremor(input_path, output_path)
    obj.find_quakes()
