"""From df filter the 'Manufacturer', 'Model' and 'Type' for every 20th row starting from 1st (row 0)."""
import pandas as pd

df = pd.read_csv("https://raw.githubusercontent.com/selva86/datasets/master/Cars93_miss.csv")
df = df.loc[::20, ["Manufacturer", "Model", "Type"]]
print(df)