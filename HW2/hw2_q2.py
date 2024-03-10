"""Replace missing values in Min.Price and Max.Price columns with their respective mean."""
import pandas as pd

df = pd.read_csv("https://raw.githubusercontent.com/selva86/datasets/master/Cars93_miss.csv")
meanMin = round(df["Min.Price"].mean(), 1)
meanMax = round(df["Max.Price"].mean(), 1)
df["Min.Price"].fillna(meanMin, inplace=True)
df["Max.Price"].fillna(meanMax, inplace=True)
print(df)