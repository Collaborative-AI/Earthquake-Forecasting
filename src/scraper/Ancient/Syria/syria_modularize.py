import csv
from csv import writer
from bs4 import BeautifulSoup
import requests
import pandas as pd
import io
from datetime import datetime, timedelta
import tabula
import sys
from pathlib import Path
from tabula.io import read_pdf


# ensure Scraper is imported no matter path the script is run
parent_dir = str(Path(__file__).resolve().parent.parent.parent.parent)
sys.path.insert(0, parent_dir)
from scraper.scraper import Scraper

class Syria_Scraper(Scraper):
    def __init__(self, input_path, output_path):
        self.input_path=input_path
        self.output_path=output_path
    def find_quakes(self):
        def merge_cells(df):
            # Merge multiple lines caused by the column o "Major affected localities"
            for i in range(len(df)):
                if pd.isnull(df.iloc[i,2]):
                    #  print("reached")
                    df.iloc[i-1,4] += (" " + df.iloc[i,4]) 
                    #  print(table_df1.iloc[i-1,4])

            # Drop rows with empty cells in the 'Date' column
            df.dropna(subset=df.columns[1], inplace=True)

            return df

        def read_pdf():

            # Replace 'path/to/your/pdf/file.pdf' with the actual path to your PDF file
            pdf_file_path = self.input_path

            # Specify the page number containing the table (e.g., page 1 is 1, page 2 is 2, etc.)
            page_number1 = 34
            page_number2 = 35
            page_number3 = 36

            # Use read_pdf() to extract the table from the PDF
            tables_part1 = tabula.read_pdf(pdf_file_path, pages=page_number1)
            tables_part2 = tabula.read_pdf(pdf_file_path, pages=page_number2)
            tables_part3 = tabula.read_pdf(pdf_file_path, pages=page_number3)

            # Assuming the table you want is the first one in the list (tables[0])
            # You can access the table data as a DataFrame
            table_df1 = tables_part1[0][1:]
            table_df2 = tables_part2[0][2:]
            table_df3 = tables_part3[0][2:]

            table_df1_merged = merge_cells(table_df1)
            table_df2_merged = merge_cells(table_df2)
            table_df3_merged = merge_cells(table_df3)

            table_df2_merged.columns = table_df1_merged.columns
            table_df3_merged.columns = table_df1_merged.columns

            # print(table_df1_merged)
            # print(table_df2_merged)
            # print(table_df3_merged)

            # Concatenate vertically (along rows)
            table_df = pd.concat([table_df1_merged, table_df2_merged])
            table_df = pd.concat([table_df, table_df3_merged])
            # print(table_df.iloc[35])

            # Convert the DataFrame to a CSV file named 'data.csv' in the current working directory
            table_df.to_csv(self.output_path, index=False)
        read_pdf()

if __name__ == '__main__':
    RELATIVE_PATH = "src/scraper/"
    obj=syria=Syria_Scraper(RELATIVE_PATH + "Ancient/Syria/The historical earthquakes of Syria.pdf", RELATIVE_PATH + "Ancient/Syria/SyriaHistoricalEarthquakes.csv")
    obj.find_quakes()