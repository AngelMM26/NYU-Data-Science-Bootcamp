import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('AB_NYC_2019.csv')
borough = {"Manhattan" : {}, "Brooklyn" : {}, "Bronx" : {}, "Queens" : {}, "Staten Island" : {}}

def updatePrice(borough, neighbourhood_group, neighbourhood, price):
    if neighbourhood not in borough[neighbourhood_group]:
        borough[neighbourhood_group][neighbourhood] = price
    else:
        borough[neighbourhood_group][neighbourhood] += price

maxRange = 48895
for currRow in range(0, maxRange):
    neighbourhood_group = df.loc[currRow]["neighbourhood_group"]
    neighbourhood = df.loc[currRow]["neighbourhood"]
    price = df.loc[currRow]["price"]
    updatePrice(borough, neighbourhood_group, neighbourhood, price)
    
print(borough)

