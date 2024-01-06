import pandas as pd
from datetime import datetime
from dateutil import parser
import numpy as np


# Read the CSV file into a Pandas DataFrame
input_file = 'SyriaHistoricalEarthquakes1.csv'  # Replace with the actual file path
output_file = 'SyriaHistoricalEarthquakes2.csv'    # Replace with the desired output file path

df = pd.read_csv(input_file)

# Drop unnecessary columns
df = df.drop(columns=['No.', 'Major affected localities', 'I0', 'H'])

# Changed column names
column_mapping = {'Date':'DateTime', 'Lat.': 'Latitude', 'Long.': 'Longitude', 'Ms':'Magnitude'}
df = df.rename(columns=column_mapping)

default_datetime = datetime(year=1900, month=12, day=29)

def convert_datetime(input_date):
    date_object = parser.parse(input_date, default=default_datetime)
    standard_format = date_object.strftime('%Y-%m-%d %H:%M:%S.%f+00:00')
    return standard_format

def clean(input):
    if input == '-':
        output = np.nan
    else:
        output = input
    return output


df['DateTime'] = df['DateTime'].apply(convert_datetime)
df['Latitude'] = df['Latitude'].apply(clean)
df['Longitude'] = df['Longitude'].apply(clean)
df['Magnitude'] = df['Magnitude'].apply(clean)

# Save the results to a new CSV file
df.to_csv(output_file, index=False)

print(f"Conversion completed. Results saved to {output_file}")