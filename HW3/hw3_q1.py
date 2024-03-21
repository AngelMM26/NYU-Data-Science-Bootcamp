import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

#Loads and reads Dataframe
url = "https://data.cityofnewyork.us/api/views/6fi9-q3ta/rows.csv?accessType=DOWNLOAD"
df = pd.read_csv(url)

#Gets the day from the hour_beginning column
df['hour_beginning'] = pd.to_datetime(df['hour_beginning'])
df['day'] = df['hour_beginning'].dt.day_name()

#Reorders the index 
df = df.sort_values(by='hour_beginning')
df.reset_index(drop=True, inplace=True)

#Fixes missing data
df['temperature'] = df['temperature'].ffill()
df['precipitation'] = df['precipitation'].ffill()
df['weather_summary'] = df['weather_summary'].ffill()

plt.figure(figsize=(10, 5))
plt.plot(df['day'], df['Pedestrians'], color='blue')
plt.title('Pedestrian Counts Over Time')
plt.xlabel('Day')
plt.ylabel('Pedestrian Count')
plt.grid(True)
plt.tight_layout()
print(plt.show())
