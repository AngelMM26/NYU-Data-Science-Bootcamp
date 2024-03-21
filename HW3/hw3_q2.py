import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

#Loads and reads Dataframe
url = "https://data.cityofnewyork.us/api/views/6fi9-q3ta/rows.csv?accessType=DOWNLOAD"
df = pd.read_csv(url)

df['hour_beginning'] = pd.to_datetime(df['hour_beginning'])

#Reorders the index 
df = df.sort_values(by='hour_beginning')
df.reset_index(drop=True, inplace=True)

#Fixes missing data
df['temperature'] = df['temperature'].ffill()
df['precipitation'] = df['precipitation'].ffill()
df['weather_summary'] = df['weather_summary'].ffill()


