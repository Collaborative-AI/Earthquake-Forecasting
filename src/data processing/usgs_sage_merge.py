import pandas as pd

# Load data
usgs_df = pd.read_csv('USGS2000-2023.csv', parse_dates=['time'])
sage_df = pd.read_csv('Sage_1973_2023.txt', delimiter='|', comment='#', skipinitialspace=True, parse_dates=['Time'])

# custom function to identify same event 
def is_same_event(row):
    for idx, sage_row in sage_df.iterrows():
        time_diff = abs((row['time'] - sage_row['Time']).total_seconds())
        lat_diff = abs(row['latitude'] - sage_row['Latitude'])
        long_diff = abs(row['longitude'] - sage_row['Longitude'])

        # Change this numbers to change how we define same events 
        if time_diff <= 10 and lat_diff <= 0.1 and long_diff <= 0.1:
            return idx
    return None

usgs_df['sage_idx'] = usgs_df.apply(is_same_event, axis=1)

# Outer join the dataframes
merged_df = pd.merge(usgs_df, sage_df, left_on='sage_idx', right_index=True, how='outer')

# Extract datetime components
merged_df['year'] = merged_df['time'].dt.year.fillna(merged_df['Time'].dt.year)
merged_df['month'] = merged_df['time'].dt.month.fillna(merged_df['Time'].dt.month)
merged_df['day'] = merged_df['time'].dt.day.fillna(merged_df['Time'].dt.day)
merged_df['hour'] = merged_df['time'].dt.hour.fillna(merged_df['Time'].dt.hour)
merged_df['min'] = merged_df['time'].dt.minute.fillna(merged_df['Time'].dt.minute)
merged_df['sec'] = merged_df['time'].dt.second.fillna(merged_df['Time'].dt.second)
merged_df['ms'] = merged_df['time'].dt.microsecond.fillna(merged_df['Time'].dt.microsecond) / 1000  # Convert to milliseconds

# Arrange columns
final_df = merged_df[['year', 'month', 'day', 'hour', 'min', 'sec', 'ms', 'latitude', 'longitude', 'depth', 'mag', 'magType', 'nst', 'gap', 'dmin', 'rms', 'net', 'id', 'horizontalError', 'depthError', 'magError', 'magNst', 'nst']]

print(final_df)

# final_df.to_csv('merged_data.csv', index=False)
