from scraper import *
from datetime import datetime
from csv import writer
import sys

if __name__ == "__main__":
    
    # Argentina Scraper
    input_path = "src/scraper/Argentina/raw/clean-catalog.xml"
    output_path = "src/scraper/Argentina/clean/Argentina Andean Earthquakes (2016-2017).csv"
    header = ["Time ID", "Magnitude", "Latitude", "Longitude", "Depth"]
    argentina=argentina(input_path, output_path, header)
    argentina.find_quakes()
    
    # Canada Scraper
    input_path = "src/scraper/Canada/raw/Canada-19850109-20240119.txt"
    output_path = "src/scraper/Canada/clean/Canada (1985-2024).csv"
    header = ''
    separator = '|'
    canada=canada(input_path, output_path, header, separator)
    canada.find_quakes_txt()
    
    # Japan Scraper
    input_path = "src/scraper/World_Tremor/japan"
    output_filename = "Japan Database (2005-2014)"
    output_path = f"src/scraper/World_Tremor/clean/{output_filename}.csv"
    obj=WorldTremor(input_path, output_path)
    obj.find_quakes()
    
    # GHEA Scraper
    input_path = "src/scraper/GHEA/raw/GHEA-data.txt"
    output_path = "src/scraper/GHEA/clean/GHEA (1000-1903).csv"
    header = ["En", "Source", "Year", "Mo", "Da", "Ho", "Mi", "Se", "Area", "Lat", "Lon",
              "LatUnc", "LonUnc", "EpDet", "Dep", "Io", "Msource", "M", "MUnc", "MType",
              "MDet", "MDPSource", "MDPn", "MDPIx", "MDPsc", "Remarks", "GEHid"]
    separator = '\t'
    ghea=GHEA(input_path, output_path, header, separator)
    ghea.find_quakes_txt(80)
    
    # NOAA Scraper
    input_path = "src/scraper/NOAA/raw/NCEI-WDS-Earthquakes.tsv"
    output_filename = "NOAA NCEI-WDS (0-2023)"
    output_path = f"src/scraper/NOAA/clean/{output_filename}.csv"
    header = ["Search Parameters", "Year", "Mo", "Dy", "Hr", "Mn", "Sec",
              "Tsu", "Vol", "Location Name", "Latitude", "Longitude", "Focal Depth (km)",
              "Mag", "MMI Int", "Deaths", "Death Description", "Missing", "Missing Description",
              "Injuries", "Injuries Description", "Damage ($Mil)", "Damage Description",
              "Houses Destroyed", "Houses Destroyed Description", "Houses Damaged",
              "Houses Damaged Description", "Total Deaths", "Total Death Description",
              "Total Missing", "Total Missing Description", "Total Injuries",
              "Total Injuries Description", "Total Damage ($Mil)", "Total Damage Description",
              "Total Houses Destroyed", "Total Houses Destroyed Description", "Total Houses Damaged",
              "Total Houses Damaged Description"]
    separator = "\t"
    noaa=NOAA_Scraper(input_path, output_path, header, separator)
    noaa.find_quakes_txt(2)
    
    # SoCal Scraper
    input_path = "src/scraper/SoCal/raw/SearchResults.txt"
    output_path = "src/scraper/SoCal/clean/SCEDC (1932-2023).csv"
    header=["Year/Month/Day", "Hour:Minute:Second", "ET", "GT",
                      "Magnitude", "M", "Latitude", "Longitude", "Depth",
                      "Q", "EVID", "NPH", "NGRM"]
    obj=Socal_File_Scraper(input_path, output_path, header)
    obj.find_quakes_txt(3)
    
    # World Tremor Scraper
    input_path = "src/scraper/World_Tremor/global"
    output_filename = "World Tremor Database (2005-2014)"
    output_path = f"src/scraper/World_Tremor/clean/{output_filename}.csv"
    obj=WorldTremor(input_path, output_path)
    obj.find_quakes()
