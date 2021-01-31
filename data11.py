#%%
import csv
import matplotlib.pyplot as plt
f = open('age3.csv')
data = csv.reader(f)

m = []
f = []

name = input('궁금한 동네를 입력해주세요: ')

for row in data:
    if name in row[0]:
        for i in range(3, 104):
            m.append(int(row[i].replace(',','')))
            f.append(int(row[i+103].replace(',','')))
        break

plt.plot(m, label="남성")
plt.plot(f, label='여성')
plt.title(name+' 지역의 성별 분포')
plt.legend()
plt.show()
# %%
import matplotlib
import matplotlib.font_manager as fm


[(f.name, f.fname) for f in fm.fontManager.ttflist if 'D2Coding' in f.name]
# %%
import csv
import matplotlib.pyplot as plt

f = open('age3.csv')
data = csv.reader(f)
result = []

name = input('궁금한 동네를 입력해주세요: ')
for row in data:
    if name in row[0]:
        for i in range(3,104):
            result.append(int(row[i].replace(',','')) - int(row[i+103].replace(',','')))
        break

plt.bar(range(101), result)
plt.show()
# %%
import matplotlib.pyplot as plt
plt.style.use('seaborn-white')
plt.scatter([1,2,3,4], [10, 30, 20, 40])
plt.grid()
plt.show()
# %%
### 버블 차트로 표현하기
import matplotlib.pyplot as plt
plt.style.use('seaborn-white')

plt.scatter([1,2,3,4], [10, 30, 20, 40], s=[100, 200, 250, 300])
plt.grid()
plt.show()
# %%
### 버블 차트로 표현하기 + 색 지정
import matplotlib.pyplot as plt
plt.style.use('seaborn-white')

plt.scatter([1,2,3,4], [10, 30, 20, 40], s=[30, 60, 90, 120], color=['red','blue', 'green','gold'])
plt.grid()
plt.show()
# %%
### 버블 차트로 표현하기 + 색 + 컬러뱌
import matplotlib.pyplot as plt
plt.style.use('seaborn-white')

plt.scatter([1,2,3,4], [10, 30, 20, 40], s=[100, 200, 250, 300], c=range(4))
plt.colorbar()
plt.grid()
plt.show()
# %%
### 랜덤한 숫자를 이용하여 산점도 표현하기
import matplotlib.pyplot as plt
import random
x = []
y = []
size = []
for i in range(100):
    x.append(random.randint(50, 100))
    y.append(random.randint(50, 100))
    size.append(random.randint(10, 100))

plt.scatter(x, y, s=size, c=size, cmap='jet', alpha=.7)
plt.colorbar()
plt.grid()
plt.show()
# %%
### 제주도의 연령대별 성별 비율을 산점도로 표현하기

