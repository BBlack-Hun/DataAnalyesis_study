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
import csv
import matplotlib.pyplot as plt
plt.style.use('seaborn-white')

f = open('age3.csv')
data = csv.reader(f)
m = []
f = []

name = input('궁금한 동네를 입력해주세요!')
for row in data:
    if name in row[0]:
        for i in range(3, 104):
            m.append(int(row[i].replace(',','')))
            f.append(int(row[i+103].replace(',','')))
        break

plt.scatter(m,f, c=range(101), alpha=.5, cmap='jet')
plt.grid()
plt.colorbar()
plt.plot(range(max(m)), range(max(m)), 'g')
plt.show()

# %%
### 제주도의 연령대별 성별 비율을 산점도로 표현하기
### 필요한 모듈 import
import csv
import math
import matplotlib.pyplot as plt

### 파일을 열어서 data에 저장
f = open('age3.csv')
data = csv.reader(f)

### 성별 값을 저장하기 위한 리스트 선언
m = list()
f = list()
size = list()

### 지역을 입력받기 위한 입력문
name = input('궁금한 동네를 입력해주세요: ')

### 파일을 열어 입력 받은 데이터를 한줄씩 반복문을 통해 실행
for row in data:
    ### 사용자가 입력한 지역이 존재할 경우
    if name in row[0]:
        for i in range(3, 104):
            ### , 붙은 문자열은 int형으로 형변환이 안되기 때문에 문자열의 replace 함수를 이용하여 ,를 없애는 과정 그리고 각 성별의 리스트에 더함
            m.append(int(row[i].replace(',','')))
            f.append(int(row[i+103].replace(',','')))
            size.append(math.sqrt(int(row[i].replace(',',''))+ int(row[i+103].replace(',','')) ))
        break
### 그래프의 스타일 지정
plt.style.use('ggplot')
### 한글 폰트 지정 저는 D2Coding font를 사용
plt.rc('font', family='D2Coding')
plt.figure(figsize=(10,5), dpi=300)
plt.title(name +' 지역의 성별 인구 그래프')
plt.scatter(m, f, s=size, c=range(101), alpha=.5, cmap='jet')
plt.colorbar()
plt.plot(range(max(m)), range(max(m)), 'g')
plt.xlabel('남성 인구수')
plt.ylabel('여성 인구수')
plt.show()
# %%
