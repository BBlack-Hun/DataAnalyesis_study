# %%
import csv
import numpy as np
import matplotlib.pyplot as plt

f = open('age2.csv')
data =csv.reader(f)
next(data)
data = list(data)
mn = 1
result_name = ''
result = 0

name = input("인구 구조가 알고 싶은 지역의 이름(읍면동 단위)을 입력해 주세요: ")

for row in data:
    if name in row[0]:
        home = np.array(row[3:], dtype=int) / int(row[2])
for row in data:
    away = np.array(row[3:], dtype=int) / int(row[2])
    s = np.sum((home-away) **2)
    if s < mn and name not in row[0]:
        mn = s
        result_name = row[0]
        result = away

plt.rc('font', family='D2Coding')
plt.title(name + ' 지역의 인구 구조')
plt.plot(home, label=name)
plt.plot(result, label=result_name)
plt.legend()
plt.show()
# %%
### 우리동네와 인구구조가 가장 비숫한 동네를 찾는 코드
import numpy as np
import csv
import matplotlib.pyplot as plt

# 데이터를 읽어온다.
f = open('age2.csv')
data = csv.reader(f)
next(data)
# 데이터를 다 읽은 후에, 다시 읽을 수 있도록 하기 위해 list로 저장한다.
data = list(data)

# 궁금한 지역의 이름을 입력받는다.
name = input('인구 구조가 알고 싶은 지역의 이름(읍면동 단위)을 입력하세요: ')
mn = 1
result_name = ''
result = 0

# 궁금한 지역의 인구구조를 저장한다.
for row in data:
    if name in row[0]:
        # row[2](=전체 인구수)로 나눠주는 이유: 비율을 구하기 위해, 인구 수 비교를 위해 비율로써 비교를 한다.
        home = np.array(row[3:], dtype=int) / int(row[2])

# 궁금한 지역의 인구 구조와 가장 비슷한 인구구조를 가진 지역을 찾는다.
for row in data:
    # 나눠주는 것인 위와 동일
    away = np.array(row[3:], dtype=int) / int(row[2])
    # 데이터를 음수로 만들지 않기 위해 제곱을 해줌
    s = np.sum((home-away) **2)
    # s가 0에 가까울 수록, 비슷한 것.. 또한 지역이 겹치는 것을 막기 위해, 조건을 추가
    if s < mn and name not in row[0]:
        mn = s
        result_name = row[0]
        result = away

# 궁금한 지역의 인구구조와 가장 비슷한 곳의 인구 구조를 시각화한다.
plt.style.use('ggplot')
plt.figure(figsize=(10,5), dpi=300)
plt.rc('font', family='D2Coding')
plt.title(name + ' 지역과 가장 비슷한 인구 구조를 가진 지역')
plt.plot(home, label=name)
plt.plot(result, label=result_name)
plt.legend()
plt.show()


# %%
