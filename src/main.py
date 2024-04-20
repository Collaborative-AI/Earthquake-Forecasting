from scraper import *
from datetime import datetime
from csv import writer
from tqdm import tqdm
import sys
import os  # Import os module

if __name__ == "__main__":
    
    # Argentina Scraper
    input_path = os.path.join("src", "scraper", "Argentina", "raw", "clean-catalog.xml")
    output_path = os.path.join("src", "scraper", "Argentina", "clean", "Argentina Andean Earthquakes (2016-2017).csv")
    header = ["Time ID", "Magnitude", "Latitude", "Longitude", "Depth"]
    argentina = Argentina(input_path, output_path, header)
    
    # Canada Scraper
    input_path = os.path.join("src", "scraper", "Canada", "raw", "Canada-19850101-20240412.txt")
    output_path = os.path.join("src", "scraper", "Canada", "clean", "Canada (1985-2024).csv")
    separator = '|'
    canada = Scraper(input_path=input_path, output_path=output_path, separator=separator)
    
    # Japan Scraper
    input_path = os.path.join("src", "scraper", "World_Tremor", "japan")
    output_path = os.path.join("src", "scraper", "World_Tremor", "clean", "Japan Database (2005-2014).csv")
    japan = WorldTremor(raw_folder=input_path, output_path=output_path)
    
    # GHEA Scraper
    input_path = os.path.join("src", "scraper", "GHEA", "raw", "GHEA-data.txt")
    output_path = os.path.join("src", "scraper", "GHEA", "clean", "GHEA (1000-1903).csv")
    separator = "\t"
    ghea = Scraper(input_path=input_path, output_path=output_path, separator=separator)
    
    # NOAA Scraper
    input_path = os.path.join("src", "scraper", "NOAA", "raw", "NOAA-20240412.tsv")
    output_path = os.path.join("src", "scraper", "NOAA", "clean", "NOAA NCEI-WDS (0-2024).csv")
    separator = "\t"
    noaa = Scraper(input_path=input_path, output_path=output_path, separator=separator)
    
    # SoCal Scraper
    input_path = os.path.join("src", "scraper", "SoCal", "raw", "SCEC_DC")
    output_path = os.path.join("src", "scraper", "SoCal", "clean", "SCEDC (1932-2024).csv")
    header = ["Year/Month/Day", "Hour:Minute:Second", "ET", "GT", "Magnitude",
              "M", "Latitude", "Longitude", "Depth", "Q", "EVID", "NPH", "NGRM"]
    socal = Socal_File_Scraper(input_path=input_path, output_path=output_path, header=header)
    
    # Turkey Scraper
    input_path = os.path.join("src", "scraper", "Turkey", "raw", "turkey_earthquakes(1915-2021).csv")
    output_path = os.path.join("src", "scraper", "Turkey", "clean", "Turkey (1915-2021).csv")
    separator = ";"
    turkey = Scraper(input_path=input_path, output_path=output_path, separator=separator)
    
    # World Tremor Scraper
    input_path = os.path.join("src", "scraper", "World_Tremor", "global")
    output_path = os.path.join("src", "scraper", "World_Tremor", "clean", "World Tremor Database (2005-2014).csv")
    world_tremor = WorldTremor(input_path, output_path)
    
    # Create a list with all the scraper objects along with what command to run
    scrapers = [argentina, canada, japan, ghea, noaa, socal, turkey, world_tremor]
    skips =    [None,      0,      None,  78,   0,    None,  0,      None]
    
    # Apply the tqdm function to the scrapers
    for i in tqdm(range(len(scrapers))):
        curr_scraper = scrapers[i]
        if skips[i] == None:
            curr_scraper.find_quakes()
        else:
            curr_scraper.find_quakes_txt(num_skips=skips[i])
    