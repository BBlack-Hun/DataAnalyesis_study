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
        rate = row[4] / (row[4]+row[6])
        if rate > mx:
            mx = rate
            mx_station = row[3] +  ' ' + row[1]

print(mx_station, round(mx*100,2))
# %%
import csv

f = open('subway.csv')
data = csv.reader(f)
next(data)

mx = [0] * 4
mx_station = ['']*4
label = ['유임승차', '유임하차', '무임승차', '무임하차']

for row in data:
    for i in range(4, 8):
        row[i] = int(row[i])
        if row[i] > mx[i-4]:
            mx[i-4] = row[i]
            mx_station[i-4] = row[3] + " " + row[1]

for i in range(4):
    print(label[i]+ ' : ' + mx_station[i], mx[i])
# %%
import csv
import matplotlib.pyplot as plt

f = open('subway.csv')
data = csv.reader(f)
next(data)

label = ['유임 승차', '유임하차', '무임 승차', '무임하차']
for row in data:
    for i in range(4, 8):
        row[i] = int(row[i])
plt.pie(row[4:8])
plt.axis('equal')
plt.show()

# %%
import csv
import matplotlib.pyplot as plt

f = open('subway.csv')
data = csv.reader(f)
next(data)

label = ['유임 승차', '유임하차', '무임 승차', '무임하차']
c = ['#14ccc0', '#389993', '#ff1c6a', '#cc14af']
plt.rc('font',family='D2Coding')
for row in data:
    for i in range(4,8):
        row[i] = int(row[i])
    plt.figure(dpi=300)
    plt.title(row[3] + ' '+ row[1])
    plt.pie(row[4:8], labels=label, colors=c, autopct='%1.f%%')
    plt.show()
# %%
### 출력할 때 출력이 안되므로,, 조심할것!
import csv
import matplotlib.pyplot as plt

f = open('subway.csv')
data = csv.reader(f)
next(data)

label = ['유임 승차', '유임하차', '무임 승차', '무임하차']
c = ['#14ccc0', '#389993', '#ff1c6a', '#cc14af']
plt.rc('font',family='D2Coding')
for row in data:
    for i in range(4,8):
        row[i] = int(row[i])
    plt.figure(dpi=300)
    plt.title(row[3] + ' '+ row[1])
    plt.pie(row[4:8], labels=label, colors=c, autopct='%1.f%%')
    plt.axis('equal')
    plt.savefig('img/'+row[3] + ' ' + row[1]+'.png')
    plt.show()
# %%
