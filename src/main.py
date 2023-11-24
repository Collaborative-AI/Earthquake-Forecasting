from scraper.New_Madrid.New_Madrid_modularize import New_Madrid_Scraper
from scraper.SoCal.SoCal_File_modularize import Socal_File_Scraper
from scraper.SoCal.SoCal_Web_modularize import Socal_Web_Scraper
from scraper.SRCMOD.SRCMOD_Modularize import SRCMOD_Scraper
from scraper.USGS.usgs_modularize import usgs_scraper
from scraper.Utah.Utah_modularize import Utah_Scraper
from datetime import datetime
from csv import writer

if __name__ == "__main__":
    input_path = "scraper/New_Madrid/New Madrid Earthquakes 1974-2023.txt"
    output_path = "scraper/New_Madrid/New Madrid Earthquakes 1974-2023.csv"
    header=['NET', 'DATE', 'O.T. (UTC)', 'LAT', 'LONG', 'DEP', \
                      'MAG', 'NPH', 'GAP', 'DMIN', 'RMS', 'SEO', 'SEH', 'SEZ',
                      'Q', 'COMMENTS']
    obj=New_Madrid_Scraper(input_path, output_path, header)
    obj.find_quakes()

    input_path = "scraper/SoCal/SearchResults.txt"
    output_path = "scraper/SoCal/Southern California Earthquakes (1932-2023).csv"
    header=["Year/Month/Day", "Hour:Minute:Second", "ET", "GT",
                      "Magnitude", "M", "Latitude", "Longitude", "Depth",
                      "Q", "EVID", "NPH", "NGRM"]
    obj=Socal_File_Scraper(input_path, output_path, header)
    obj.find_quakes_txt()

    #url = "https://service.scedc.caltech.edu/cgi-bin/catalog/catalog_search.pl?outputfmt=scec&start_year=1932&start_month=01&start_day=01&start_hr=00&start_min=00&start_sec=00&end_year=2023&end_month=07&end_day=25&end_hr=00&end_min=00&end_sec=00&min_mag=1&max_mag=9.9&min_depth=0&max_depth=1000.0&south_latd=30.0&north_latd=39.0&west_long=-124.0&east_long=-111.0&etype=eq&gtype=l&file_out=N"
    #output_path = "scraper/SoCal/Southern California Earthquakes From Web (1932-2023).csv"
    #header=["Year/Month/Day", "Hour:Minute:Second", "ET", "GT","Magnitude", "M",  "Latitude", "Longitude", "Depth", "Q", "EVID", "NPH", "NGRM"]
    #obj=Socal_Web_Scraper(url, output_path, header)
    #obj.find_quakes_web()

    output_path="scraper/SRCMOD/srcmod.csv"
    url="http://equake-rc.info/SRCMOD/searchmodels/allevents/"
    header=["Earthquake ID", "Region", "Date (dd/mm/yyyy)", "Filnn-Engdahl Region", \
                " ", "Magnitude", "Latitude (°N)", "Longitude (°E)", "Depth (km)", \
                "Author", "Upload Date (mm/yyyy)"]
    obj=SRCMOD_Scraper(output_path, url, header)
    obj.find_quakes_web()

    url="https://earthquake.usgs.gov/fdsnws/event/1/query"
    start_date=datetime(1800, 1, 1)
    end_date=datetime(2023, 6, 12)
    obj=usgs_scraper(url, start_date, end_date)
    earthquake_data =obj.download_data()
    earthquake_data.to_csv("scraper/USGS/earthquake_data.csv", index=False)

    input_path = "scraper/Utah/detections.txt"
    output_path = "scraper/Utah/Mineral Mountains, Utah 2016-19.csv"
    header = ["Year", "Origin Time (UTC)", "Latitude", "Longitude",
                      "Depth", "Template Event Magnitude", "Detection Magnitude",
                      "Event Template ID", "Detection ID", "Correlation Coefficient"]
    obj=Utah_Scraper(input_path, output_path, header)
    obj.find_quakes_txt()