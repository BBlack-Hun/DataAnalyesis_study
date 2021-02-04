#%%
import csv
f = open('subway.csv')
data = csv.reader(f)

for row in data:
    print(row)
