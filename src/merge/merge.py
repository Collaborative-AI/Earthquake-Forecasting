# import helper functions for data merging
import sys
sys.path.append("src/merge")

# run on python 3.11.2
from helper import merge_group

"""
merge.py

This python file merges earthquake catalogs by geographical regions (e.g.,
North America, Asia), then merges the region datasets together into one
worldwide dataset.

The output dataset will be found in the src/merge/ folder, and the
resulting CSV is guaranteed to be:

1. Sorted in chronological order
2. Distinct (aka no duplicates)

"""

"""
STEP 1:
Find all the filepaths to all datasets unrelated to USGS and SAGE.
Modify the SCRAPER_PATH if your working directory isn't the root.
"""

SCRAPER_PATH = "src/scraper/"
csv_files = ["Argentina/clean/Argentina Andean Earthquakes (2016-2017).csv",
             "Canada/clean/Canada (1985-2024).csv",
             "East Africa/clean/East Africa Rift System (1994-2022).csv",
             "GHEA/clean/GHEA (1000-1903).csv",
             "Intensity/clean/U.S. Earthquake Intensity Database (1638-1985).csv",
             "NOAA/clean/NOAA NCEI-WDS (0-2023).csv",
             "Pacific Northwest/clean/PNW Tremors (2009-2023).csv",
             "SoCal/clean/SCEDC (1932-2023).csv",
             "South Asia/clean/South Asia (1900-2014).csv",
             "Texas/clean/Texas (2016-2023).csv",
             "Turkey/clean/Turkey (1915-2021).csv",
             "World Tremor/clean/World Tremor Database (2005-2014).csv"]

csv_files = [SCRAPER_PATH + csv_file for csv_file in csv_files]

"""
STEP 2:
Define the output path and run the merge function.
"""
output_path = "src/merge/Various-Catalogs.csv"
merge_group(csv_files, output_path)