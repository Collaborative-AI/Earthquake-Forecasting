from scraper import *
from datetime import datetime
from csv import writer
import sys

if __name__ == "__main__":
    '''
    input_path = "scraper/Argentina/raw/clean-catalog.xml"
    output_path = "scraper/Argentina/clean/Argentina Andean Earthquakes (2016-2017).csv"
    header = ["Time ID", "Magnitude", "Station Count", "Author", "Publication Time"]
    argintina=argintina(input_path, output_path,header)
    argintina.find_quakes()

    canada_1=canada("scraper/Canada/raw/Canada-19850109-20240117.txt", "scraper/Canada/clean/Canada (1985-2024).csv", '','|')
    canada_1.find_quakes_txt()

    ghea=GHEA("scraper/GHEA/raw/GHEA-data.txt", "scraper/GHEA/clean/GHEA (1000-1903).csv", ["En", "Source", "Year", "Mo", "Da", "Ho", "Mi", "Se", "Area", "Lat", "Lon", "LatUnc", "LonUnc", "EpDet", "Dep", "Io", "Msource", "M", "MUnc", "MType", "MDet", "MDPSource", "MDPn", "MDPIx", "MDPsc", "Remarks", "GEHid"],"\t")
    ghea.find_quakes_txt()

    input_path = "scraper/NOAA/raw/NCEI-WDS-Earthquakes.tsv"
    
    output_filename = "NOAA NCEI-WDS (0-2023)"
    output_path = f"scraper/NOAA/clean/{output_filename}.csv"
    
    noaa=NOAA_Scraper(input_path, output_path)
    noaa.find_quakes()

    input_path = "scraper/Pacific_Northwest/raw/pacific-northwest-tremors-2009-2023.csv"
    output_filename = "PNW Tremors (2009-2023)"
    output_path = f"scraper/Pacific_Northwest/clean/{output_filename}.csv"
    PNW=PNW_Scraper(input_path, output_path)
    PNW.find_quakes()

    input_path = "scraper/SoCal/raw/SearchResults.txt"
    output_path = "scraper/SoCal/clean/SCEDC (1932-2023).csv"
    header=["Year/Month/Day", "Hour:Minute:Second", "ET", "GT",
                      "Magnitude", "M", "Latitude", "Longitude", "Depth",
                      "Q", "EVID", "NPH", "NGRM"]
    obj=Socal_File_Scraper(input_path, output_path, header)
    obj.find_quakes_txt(3)

    input_path = "scraper/South_Asia/raw/11069_2016_2665_MOESM2_ESM.csv"
    
    output_filename = "South Asia (1900-2014)"
    output_path = f"scraper/South_Asia/clean/{output_filename}.csv"
    
    SouthAsia=SouthAsia_Scraper(input_path, output_path)
    SouthAsia.find_quakes()
    '''
    input_path = "scraper/East_Africa/raw/SouthEARS_EarthquakeCatalog.csv"
    output_filename = "East Africa Rift System (1994-2022)"
    output_path = f"scraper/East_Africa/clean/{output_filename}.csv"
    
    EastAfrica=EastAfrica(input_path, output_path)
    EastAfrica.find_quakes()

    input_path = "scraper/Intensity/raw/eqint_tsqp.csv"
    
    output_filename = "U.S. Earthquake Intensity Database (1638-1985)"
    output_path = f"scraper/Intensity/clean/{output_filename}.csv"
    
    intensity=Intensity(input_path, output_path)
    intensity.find_quakes()

    input_path = "scraper/Texas/raw/texnet_events.csv"
    
    output_filename = "Texas (2016-2023)"
    output_path = f"scraper/Texas/clean/{output_filename}.csv"
    
    texas=TexasScraper(input_path, output_path)
    texas.find_quakes()
    
    input_path = "scraper/Turkey/raw/turkey_earthquakes(1915-2021).csv"
    
    output_filename = "Turkey (1915-2021)"
    output_path = f"scraper/Turkey/clean/{output_filename}.csv"
    
    turkey=TurkeyScraper(input_path, output_path)
    turkey.find_quakes()

    output_filename = "World Tremor Database (2005-2014)"
    output_path = f"scraper/World_Tremor/clean/{output_filename}.csv"
    
    raw_folder = "scraper/World_Tremor/raw"
    worldtremor=WorldTremor(raw_folder, output_path)
    worldtremor.find_quakes()