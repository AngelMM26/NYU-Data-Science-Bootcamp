import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('AB_NYC_2019.csv')

def updatePrice(boroughs, neighbourhood_group, neighbourhood, price):
    if neighbourhood not in boroughs[neighbourhood_group]:
        boroughs[neighbourhood_group][neighbourhood] = {"totalSum" : price, "count": 1}
    else:
        boroughs[neighbourhood_group][neighbourhood]["totalSum"] += price
        boroughs[neighbourhood_group][neighbourhood]["count"] += 1

boroughs = {"Manhattan" : {}, "Brooklyn" : {}, "Bronx" : {}, "Queens" : {}, "Staten Island" : {}}
maxRange = 48895
for currRow in range(0, maxRange):
    neighbourhood_group = df.loc[currRow]["neighbourhood_group"]
    neighbourhood = df.loc[currRow]["neighbourhood"]
    price = df.loc[currRow]["price"]
    updatePrice(boroughs, neighbourhood_group, neighbourhood, price)
    
for borough in boroughs:
    for neighbourhood in boroughs[borough]:
        avgPrice = (boroughs[borough][neighbourhood]["totalSum"])/(boroughs[borough][neighbourhood]["count"])
        boroughs[borough][neighbourhood]["avgPrice"] = round(avgPrice,2)

print(boroughs)
