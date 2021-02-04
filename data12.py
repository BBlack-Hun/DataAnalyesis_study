#%%
import csv
f = open('subway.csv')
data = csv.reader(f)

for row in data:
    print(row)

# %%
import csv

f = open('subway.csv')
data =csv.reader(f)
next(data)
for row in data:
    for i in range(4, 8):
        row[i] = int(row[i])
    print(row)
# %%
import csv
import matplotlib.pyplot as plt


