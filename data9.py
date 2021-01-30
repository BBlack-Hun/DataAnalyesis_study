#%%
import csv

f= open('age2.csv')
data = csv.reader(f)

for row in data:
    print(row)
# %%
import csv

f = open('age2.csv')
data = csv.reader(f)

for row in data:
    if '서울특별시 구로구 신도림동(1153051000)' == row[0]:
        print(row)
# %%
print('신도림' in '서울특별시 구로구 신도림동(1153051000)')
print('1153' in '서울특별시 구로구 신도림동(1153051000)')
print('()' in '서울특별시 구로구 신도림동(1153051000)')
# %%
import csv

f = open('age2.csv')
data = csv.reader(f)

for row in data:
    if '신도림' in row[0]:
        print(row)
# %%
import csv

f = open('age2.csv')
data = csv.reader(f)


for row in data:
    ### 신도림이 포함된 행정구역 찾기
    if '신도림' in row[0]:
        ### 앞의 목록을 제외한 0세부터 100세까지의 나이 출력
        for i in row[3:]:
            print(i)
# %%
import csv

f = open('age2.csv')
data = csv.reader(f)
### 빈 리스트 만들기
result = []

for row in data:
    if '신도림' in row[0]:
        for i in row[3:]:
            ### 해당되는 데이터틀 리스트에 저장한다.
            result.append(i)
### 결과 출력
print(result)
# %%
import matplotlib.pyplot as plt
import csv
f = open('age2.csv')
data = csv.reader(f)
### 빈 리스트 만들기
result = []

for row in data:
    if '신도림' in row[0]:
        for i in row[3:]:
            ### 해당되는 데이터틀 리스트에 저장한다.
            result.append(int(i))
### 결과 출력
print(result)
plt.style.use("ggplot")
plt.plot(result)
plt.show()
# %%
import matplotlib.pyplot as plt
import csv
f = open('age2.csv')
data = csv.reader(f)
### 빈 리스트 만들기
result = []

str = input("인구 구조가 알고 싶은 지역의 이름(읍면동 단위)을 입력해 주세요.: ")

for row in data:
    if str in row[0]:
        for i in row[3:]:
            ### 해당되는 데이터틀 리스트에 저장한다.
            result.append(int(i))
### 결과 출력
#print(result)
plt.style.use("ggplot")
plt.rc("font", family="NanumGothic")
plt.title(str+"지역의 인구 구조")
plt.plot(result)
plt.show()
# %%
import matplotlib.pyplot as plt

plt.bar([0,1,2,4,6,10],[1,2,3,6,7,8])
plt.show()
# %%
import matplotlib.pyplot as plt

plt.bar(range(6), [1,2,3,5,6,7])
plt.show()
# %%
import csv
import matplotlib.pyplot as plt

f = open('age2.csv')
data = csv.reader(f)

result= []

for row in data:
    if '신도림' in row[0]:
        for i in row[3:]:
            result.append(int(i))

plt.bar(range(101), result)
plt.show()
# %%
plt.barh(range(101), result)
plt.show()
# %%
### 항아리 모양 그래프 그리기 - 데이터 정제-1
### 성별별로 데이터를 나눠서 저장
import csv

f = open("age3.csv")
data = csv.reader(f)
m = []
f = []
for row in data:
    if '신도림' in row[0]:
        for i in range(0, 101):
            m.append(int(row[i+3]))
            f.append(int(row[-(i+1)]))

f.reverse()

print("남자 리스트 ", m)
print("여자 리스트 ", f)
# %%
### 항아리 모양 그래프 그리기 - 데이터 정제-1
### 성별별로 데이터를 나눠서 저장