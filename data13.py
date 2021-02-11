#%%
import csv

f = open('subwaytime.csv')
data = csv.reader(f)

for row in data:
    for i in range(4,8):
        row[i] = int(row[1])
    print(row)
# %%
import csv
import matplotlib.pyplot as plt

f = open('subwaytime.csv')
data = csv.reader(f)
next(data)
next(data)

for row in data:
    row[4:] = map(int, row[4:])
    print(row)
# %%
### 출근시간대 사람들이 가장 많이 타고 내리는 역은 어딜까용?
import csv
import matplotlib.pyplot as plt

f = open("subwaytime.csv")
data = csv.reader(f)
next(data)
next(data)

result = []

for row in data:
    row[4:] = map(int, row[4:])
    #result.append(row[10])
    # 7~9시까지 승차인원을 합치기 위한 코드 수정
    result.append(sum(row[10:15:2]))
print(len(result))
print(result)
result.sort()
plt.bar(range(len(result)), result)
plt.show()
# %%
import csv

f = open('subwaytime.csv')
data = csv.reader(f)
next(data)
next(data)

# 최대값을 저장하기 위한 변수 초기화
mx = 0
# 최대값을 갖는 역 이름 저장 변수 초기화
mx_station = ''
# 최대값을 찾기
for row in data:
    row[4:] = map(int, row[4:])
    if sum(row[10:15:2]) > mx:
        mx = sum(row[10:15:2])
        mx_station = row[3] +  '('+row[1]+')'
print(mx_station, mx)
# %%
### 출근 시간대 사람들이 가장 많이 타고 내리는 역 찾기
import csv

f = open('subwaytime.csv')
data = csv.reader(f)
next(data)
next(data)

# 변수 초기화
mx = 0
mx_station = ''
for row in data:
    row[4:] = map(int, row[4:])
    a = row[11:16:2]
    if sum(a) > mx :
        mx = sum(a)
        mx_station = row[3] +  '('+row[1]+')'

print(mx_station, mx)


# %%
### 밤 11시에 사람들이 가장 많이 타고 내리는 역을 찾는 코드
import csv

f = open('subwaytime.csv')
data = csv.reader(f)
next(data)
next(data)

mx = 0
mx_station = ''
t = int(input('몇 시의 승차 인원이 가장 많은 역이 궁금하세요?: '))

for row in data:
    row[4:] = map(int, row[4:])
    # 입력 받은 시각의 승차 인원 값 추출하기
    a = row[4+(t-4)*2]
    # 모든 데이터 탐색
    if a > mx:
        mx = a
        mx_station = row[3] +  '('+row[1]+')'
print(mx_station, mx)
# %%
### 시간대별로 사람들이 가장 많이 타고 내리는 역은 어디일까?
import csv
import matplotlib.pyplot as plt

f = open('subwaytime.csv')
data = csv.reader(f)
next(data)
next(data)
mx = [0] * 24
mx_station = [''] * 24
for row in data:
    row[4:] = map(int, row[4:])
    for j in range(24):
        # j와 인덱스 번호 사이의 관계식을 사용
        a = row[j*2+4]
        if a > mx[j]:
            mx[j] = a
            mx_station[j] = row[3] +  '('+str(j+4)+'시)'
print(mx_station)
print(mx)

plt.rc('font', family='D2Coding')
plt.bar(range(24), mx)
plt.xticks(range(24), mx_station, rotation=90)
plt.show()
# %%
### 시간대별로 하차 인원이 가장 많은 역을 찾는 코드
import csv
import matplotlib.pyplot as plt

f = open('subwaytime.csv')
data = csv.reader(f)
next(data)
next(data)

mx = [0] * 24
mx_station = [''] * 24

for row in data:
    row[4:] = map(int, row[4:])
    for j in range(24):
        b = row[5 + j * 2]
        if b > mx[j]:
            mx[j] = b
            mx_station[j] = row[3] +  '('+str(j+4)+'시)'

plt.rc('font', family='D2Coding')
plt.bar(range(24), mx, color='b')
plt.xticks(range(24), mx_station, rotation=90)
plt.show()
# %%
### 모든 지하철역에서 시간대별 승하차 인원을 모두 더하면?
import csv
import matplotlib.pyplot as plt

f = open('subwaytime.csv')
data = csv.reader(f)

next(data)
next(data)

# 승차 인원 초기화
s_in = [0] * 24
s_out = [0] * 24

for row in data:
    row[4:] = map(int, row[4:])
    for i in range(24):
        s_in[i] += row[4+i*2]
        s_out[i] += row[5+i*2]

plt.rc('font', family='D2Coding')
plt.title('지하철 시간대별 승하차 인원 추이')
plt.plot(s_in, label='승차')
plt.plot(s_out, label='하차')
plt.legend()
plt.xticks(range(24), range(4, 28))
plt.show()
# %%
