# import all scraper functions
import sys
# sys.path.append("src/data_processing/")
from data_processing import *
import os

RELATIVE_PATH = ""

if __name__ == "__main__":
    src0 = RELATIVE_PATH + "USGS2000-2023.csv"
    src1 = RELATIVE_PATH + "USGS1950-1999.csv"
    src2 = RELATIVE_PATH + "SAGE_1973_2023.txt"
    obj=Processing([src0, src1, src2])
    obj.data_merge()