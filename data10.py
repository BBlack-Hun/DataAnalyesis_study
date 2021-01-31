#%%
### 제주도에는 여성의 비율이 더 높을까?
### 필요 모듈 import
import csv
import matplotlib.pyplot as plt
plt.style.use('ggplot')

### csv 파일을 불러와 data에 저장
f = open('age3.csv')
data = csv.reader(f)

### 각 성별의 인구 분포를 저장할 리스트 선언
m = []
f = []

### 찾고 싶은 지역을 입력받기 위한 name 변수 선언 및 input
name = input('찾고 싶은 지역의 이름을 알려주세요: ')

### 반복문 시작, 데이터를 한줄한줄 읽어옴
for row in data:
    ### 사용자로부터 입력받은 지역이 row의 0번 인덱스에 존재할 경우(0번 인덱스는 시도군읍면동으로 데이터의 지역을 나타낸다.)
    if name in row[0]:
        for i in row[3: 104]:
            m.append(int(i.replace(',','')))
        for i in row[106:]:
            f.append(-int(i.replace(',','')))
        break
plt.figure(figsize=(10,5), dpi=300)
plt.rc('font', family='D2Coding')
plt.rcParams['axes.unicode_minus'] = False
plt.title(name+' 지역의 남녀 인구 분포')
plt.barh(range(len(m)), m, label='남성')
plt.barh(range(len(f)), f, label='여성')
plt.legend()
plt.show()
# %%
import matplotlib.pyplot as plt
plt.pie([10,20])
plt.show()
# %%
import matplotlib.pyplot as plt
size = [2441, 2312, 1031, 1233]
plt.axis('equal')
plt.pie(size)
plt.show()
# %%
### 레이블 추가하기
### 관련 모듈 import
import matplotlib.pyplot as plt
### 한글 표시를 위한 폰트 적용
plt.rc('font', family='NanumGothic')
### 데이터
size = [2441, 2312, 1031, 1233]
### 라벨
label = ['A형', 'B형', 'AB형', 'O형']
plt.axis('equal')
plt.pie(size, labels=label)
plt.show()
# %%
### 비율 및 범례 표시
### 관련 라이브러리 import
import matplotlib.pyplot as plt
### 한글 사용을 위한 font
plt.rc('font', family='NanumGothic')
size = [2441, 2312, 1031, 1233]
label = ['A형', 'B형', 'AB형', 'O형']
plt.axis('equal')
plt.pie(size, labels=label, autopct='%.1f%%')
plt.legend()
plt.show()
# %%
### 색 및 돌출 효과
### 관련 라이브러리 import
import matplotlib.pyplot as plt
### 한글 사용을 위한 font
plt.rc('font', family='NanumGothic')
### 데이터
size = [2441, 2312, 1031, 1233]
### 라벨
label = ['A형', 'B형', 'AB형', 'O형']
### 각 데이터의 색
color = ['darkmagenta', 'deeppink', 'hotpink', 'pink']
### 사실 이거 잘 모르겠음.....
plt.axis('equal')
### explode로 돌출 효과, colors로 각 조각마다 색부여
plt.pie(size, labels=label, autopct='%.1f%%', colors=color, explode=(0,0,0.1,0))
### 범례
plt.legend()
plt.show()
# %%
### 제주도의 성별 인구 비율 표현하기
### 필요한 모듈 import
import csv
import matplotlib.pyplot as plt

### 데이터 불러오기
f = open('age3.csv')
data = csv.reader(f)

### 필요한 데이터를 저장하기 위한 list 선언
size = []

### 사용자가 원하는 지역의 데이터를 추출하기 위한 입력문
name = input('찾고 싶은 지역의 이름을 알려주세요: ')

### 반복문을 통하여 데이터 추출
for row in data:
    ### 사용자가 입력한 지역에 해당하는 데이터 중
    if name in row[0]:
        ### 남녀 변수 초기화
        m = 0
        f = 0
        ### 0~101세까지
        for i in range(101):
            ### 각 성별 별로 더한다. Replace를 해주는 이유는, 쉼표(,)가 들어가 있으면 형변환이 안됨.
            m += int(row[i+3].replace(',',''))
            f += int(row[i+106].replace(',',''))
        break
### size
size.append(m)
size.append(f)
print(size)

color=['crimson', 'darkcyan']
plt.rc('font', family='D2Coding')
plt.axis('equal')
plt.pie(size, labels=['남', '여'], autopct="%.1f%%", colors=color, startangle=90)
plt.title(name+' 지역의 남녀 성별 비율')
plt.show()