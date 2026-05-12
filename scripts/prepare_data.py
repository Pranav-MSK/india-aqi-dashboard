import pandas as pd

# Load raw data
df = pd.read_csv('data/city_day.csv')
print(f"Raw data: {df.shape}")

# Filter to major metro cities
cities = [
    'Delhi', 'Mumbai', 'Chennai', 'Kolkata', 'Bengaluru',
    'Hyderabad', 'Ahmedabad', 'Jaipur', 'Gurugram'
]
df = df[df['City'].isin(cities)]

# Drop niche pollutant columns
df = df.drop(columns=['NO', 'NOx', 'NH3', 'Benzene', 'Toluene', 'Xylene'])

# Drop rows with any null values
df = df.dropna()
print(f"After cleaning: {df.shape}")
print(f"\nRows per city:\n{df['City'].value_counts()}")
print(f"\nDate range: {df['Date'].min()} to {df['Date'].max()}")

# Save cleaned data
df.to_csv('data/aqi_metro.csv', index=False)
print("\nSaved to data/aqi_metro.csv")
