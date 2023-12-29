from scraper import *
from datetime import datetime
from csv import writer
import sys

if __name__ == "__main__":
    input_path='scraper/Ancient/Syria/The historical earthquakes of Syria.pdf'
    output_path='scraper/Ancient/Syria/SyriaHistoricalEarthquakes.csv'
    obj=Syria_Scraper(input_path, output_path)
    obj.read_pdf()

    obj=wiki_Scraper('https://en.wikipedia.org/wiki/List_of_historical_earthquakes','scraper/Ancient/Wikipedia/WikiHistoricalEarthquakes.csv')
    obj.find_earthquake()

    input_path = "scraper/Argentina/clean-catalog.xml"
    output_path = "scraper/Argentina/Argentina Andean Earthquakes (2016-2017).csv"
    header = ["Time ID", "Magnitude", "Station Count", "Author", "Publication Time"]
    argintina=argintina(input_path, output_path,header)
    argintina.find_quakes()

    canada_1=canada("scraper/Canada/Canada-19850109-20230621.txt", "scraper/Canada/Canada-19850109-20230621.csv", '','|')
    canada_1.find_quakes_txt()

    corinth_1 = corinth("scraper/Corinth/Marathias_seq.txt", "scraper/Corinth/Corinth Gulf 2020-21 Seismic Crisis.csv", ["Year", "Origin Time", "Latitude", "Longitude", "Depth",
                      "Magnitude", "Decimal Years", "Time Relative to First Earthquake",
                      "Event ID", "Cluster ID (sorted by #events)",
                      "Cluster ID (by time)", "Multiplet ID", "#events in Multiplet",
                      "E-W horizontal error", "N-S horizontal error",
                      "Vertical error"], None)
    corinth_1.find_quakes_txt()
    # GHEA not working
    '''
    ghea=GHEA("scraper/GHEA/GHEA-data.txt", "scraper/GHEA/GHEA Data 1000-1903.csv", ["En", "Source", "Year", "Mo", "Da", "Ho", "Mi", "Se",
                          "Area", "Lat", "Lon", "LatUnc", "LonUnc", "EpDet", "Dep",
                          "Io", "Msource", "M", "MUnc", "MType", "MDet", "MDPSource",
                          "MDPn", "MDPIx", "MDPsc", "Remarks", "GEHid"],"\t")
    ghea.find_quakes_txt()
    '''
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
    obj.find_quakes_txt(3)

    # socal web not working
    '''
    url = "https://service.scedc.caltech.edu/cgi-bin/catalog/catalog_search.pl?outputfmt=scec&start_year=1932&start_month=01&start_day=01&start_hr=00&start_min=00&start_sec=00&end_year=2023&end_month=07&end_day=25&end_hr=00&end_min=00&end_sec=00&min_mag=1&max_mag=9.9&min_depth=0&max_depth=1000.0&south_latd=30.0&north_latd=39.0&west_long=-124.0&east_long=-111.0&etype=eq&gtype=l&file_out=N"
    #output_path = "scraper/SoCal/Southern California Earthquakes From Web (1932-2023).csv"
    header=["Year/Month/Day", "Hour:Minute:Second", "ET", "GT","Magnitude", "M",  "Latitude", "Longitude", "Depth", "Q", "EVID", "NPH", "NGRM"]
    obj=Socal_Web_Scraper(url, output_path, header)
    obj.find_quakes_web()
    '''
    output_path="scraper/SRCMOD/srcmod.csv"
    url="http://equake-rc.info/SRCMOD/searchmodels/allevents/"
    header=["Earthquake ID", "Region", "Date (dd/mm/yyyy)", "Filnn-Engdahl Region", \
                " ", "Magnitude", "Latitude (°N)", "Longitude (°E)", "Depth (km)", \
                "Author", "Upload Date (mm/yyyy)"]
    obj=SRCMOD_Scraper(output_path, url, header)
    obj.find_quakes_web()
    
    # usgs not working
    '''
    url="https://earthquake.usgs.gov/fdsnws/event/1/query"
    start_date=datetime(1800, 1, 1)
    end_date=datetime(2023, 6, 12)
    obj=usgs_scraper(url, start_date, end_date)
    earthquake_data =obj.download_data()
    earthquake_data.to_csv("scraper/USGS/earthquake_data.csv", index=False)
    '''
    input_path = "scraper/Utah/detections.txt"
    output_path = "scraper/Utah/Mineral Mountains, Utah 2016-19.csv"
    header = ["Year", "Origin Time (UTC)", "Latitude", "Longitude",
                      "Depth", "Template Event Magnitude", "Detection Magnitude",
                      "Event Template ID", "Detection ID", "Correlation Coefficient"]
    obj=Utah_Scraper(input_path, output_path, header)
    obj.find_quakes_txt()