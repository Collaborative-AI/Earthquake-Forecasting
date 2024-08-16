# SmartQuake

SmartQuake is a research project to predict earthquake on a global scale with the latest machine learning technologies. It incorporates data from 14 datasets from worldwide, creating a dataset that can also be used for future research in earthquake prediction. 

# Dataset Scraping

## Scraping the dataset
- From the Google Drive, download the raw datasets. The datasets should be placed respectively under `src/scraper/.../raw` folder.
- After installing the dependencies by `pip install requirements.txt`, run `python src/main.py`
- The scraped datasets will be placed under the path `src/scraper/.../clean`

# Data Processing

## Earthquake Dataset Merger

## Overview
This tool merges various earthquake catalogs from different geographical regions into a single, worldwide dataset. The output is a CSV file that is sorted chronologically and contains no duplicates.

## Requirements
- Python 3.11.2

## Setup
1. Ensure Python 3.11.2 is installed on your system.
2. Clone the repository to your local machine.

## Usage
1. Place all earthquake catalog datasets within the `src/data_processing/processed/` directory. Ensure that datasets from USGS and SAGE are excluded.

2. Run `merge.py` to merge the datasets:  [python merge.py]

3. The merged dataset will be saved to `src/merge/Various-Catalogs.csv`.

## Details
- The script first finds all the filepaths to datasets in the `src/data_processing/processed/` folder.
- It then uses the `merge_group` function from `src/merge/helper.py` to merge these files.
- The final output is stored in the `src/merge/` folder, ensuring the data is sorted and distinct.
