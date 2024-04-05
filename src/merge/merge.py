# import helper functions for data merging
import sys
sys.path.append("src/merge")
import os

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

SCRAPER_PATH = "src/data_processing/processed"
csv_files = [f for f in os.listdir(SCRAPER_PATH)]
csv_files = [os.path.join(SCRAPER_PATH, csv_file) for csv_file in csv_files]

"""
STEP 2:
Define the output path and run the merge function.
"""
output_path = "src/merge/Various-Catalogs.csv"
merge_group(csv_files, output_path)