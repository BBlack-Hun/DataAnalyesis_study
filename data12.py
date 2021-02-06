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
f = open('subway.csv')
data = csv.reader(f)
next(data)

mx = 0
rate = 0
for row in data:
    for i in range(4, 8):
        row[i] = int(row[i])
    # 0값이 존재하므로, 오류가 발생
    rate = row[4] / row[6]
    if rate > mx:
        mx = rate

print(mx)
# %%
import csv

f = open('subway.csv')
data = csv.reader(f)
next(data)

mx = 0
rate = 0
for row in data:
    for i in range(4, 8):
        row[i] = int(row[i])
    if row[6] != 0:
        rate = row[4] / row[6]
        if rate > mx:
            mx = rate
            print(row, round(rate, 2))
print(mx)
# %%
import csv

f = open('subway.csv')
data = csv.reader(f)
next(data)

mx = 0
rate = 0
for row in data:
    for i in range(4, 8):
        row[i] = int(row[i])
    if row[6] != 0 and (row[4] + row[6]) > 100000:
        rate = row[4] / (row[4] + row[6])
        if rate > mx:
            mx = rate
            print(row, round(rate, 2))
print(mx)
# %%
import csv

f = open('subway.csv')
data = csv.reader(f)
next(data)

mx = 0 
rate = 0
mx_station = ''

for row in data:
    for i in range(4, 8):
        row[i] = int(row[i])
    if row[6] != 0 and (row[4]+row[6]) > 100000:
        rate = rate[4] / (row[4] + row[6])
        if rate > mx:
            mx = rate
            

    