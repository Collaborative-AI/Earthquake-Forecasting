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
Merge North America Batch
Includes the following earthquakes:
- Canada
- NCEDC
- New Madrid
- Pacific Northwest (PNW)
- Southern California (SoCal)
- Texas
- Utah (Mineral Mountains)
"""

csv_files = ["Canada/clean/Canada (1985-2024).csv",
             "NCEDC/clean/NCEDC (1984-2023).csv",
             "New Madrid/clean/New Madrid (1974-2023).csv",
             "Pacific Northwest/clean/PNW Tremors (2009-2023).csv",
             "SoCal/clean/SCEDC (1932-2023).csv",
             "Texas/clean/Texas (2016-2023).csv",
             "Utah/clean/Utah (2016-2019).csv"]