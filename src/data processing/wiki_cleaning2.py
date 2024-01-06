import pandas as pd
from datetime import datetime
from dateutil import parser

def convert_to_standard_datetime(input_date):
    try:
        # Check if the date has a day component
        date_object = datetime.strptime(input_date, '%Y-%m-%d %H:%M:%S')
        # if input_date.count('-') == 2:
        #     # Try parsing the date with the known format
        #     date_object = datetime.strptime(input_date, '%Y-%m-%d %H:%M:%S')
        # else:
        #     # Stays the same (these entries were manually converted)
        #     return input_date
    except ValueError:
        try:
            # Try parsing with dateutil.parser for other formats
            date_object = parser.parse(input_date)
        except ValueError:
            # Handle the case where the input date is not in a recognizable format
            return "Invalid Date"

    # Format the date object in a standard datetime format
    standard_format = date_object.strftime('%Y-%m-%d %H:%M:%S')
    

    return standard_format
# Read the CSV file into a Pandas DataFrame
input_file = 'WikipediaEarthquakes2.csv'  # Replace with the actual file path
output_file = 'WikipediaEarthquakes3.csv'    # Replace with the desired output file path

df = pd.read_csv(input_file)

# Remove the BC entries
df = df.iloc[7:].reset_index(drop=True)

# Apply the conversion function to the "DateTime" column
df['DateTime'] = df['DateTime'].apply(convert_to_standard_datetime)

print(df['DateTime'])

# print(convert_to_standard_datetime(df['DateTime'][0]))

# Save the results to a new CSV file
df.to_csv(output_file, index=False)

print(f"Conversion completed. Results saved to {output_file}")
