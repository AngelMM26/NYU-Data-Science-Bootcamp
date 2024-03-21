import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

#Loads and reads Dataframe
url = "https://data.cityofnewyork.us/api/views/6fi9-q3ta/rows.csv?accessType=DOWNLOAD"
df = pd.read_csv(url)

#Gets the hour
df['hour_beginning'] = pd.to_datetime(df['hour_beginning'])
df['hour'] = df['hour_beginning'].dt.hour

#Reorders the index 
df = df.sort_values(by='hour_beginning')
df.reset_index(drop=True, inplace=True)

#Fixes missing data
df['temperature'] = df['temperature'].ffill()
df['precipitation'] = df['precipitation'].ffill()
df['weather_summary'] = df['weather_summary'].ffill()

def getTimeOfDay(hour):
    if(0 <= hour < 6):
        return 'Night'
    elif(6 <= hour < 12):
        return 'Morning'
    elif(12 <= hour < 18):
        return 'Afternoon'
    else:
        return 'Evening'

df['time_of_day'] = df['hour'].apply(getTimeOfDay)
print(df['time_of_day'])
