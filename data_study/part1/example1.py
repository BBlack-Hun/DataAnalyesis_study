#%%
from numpy import trim_zeros
import pandas as pd
from pandas.io.formats.style import has_mpl

# key:value 쌍으로 딕셔너리를 만들고, 변수 dict_data에 저장
dict_data = {'a':1, 'b': 2, 'c':3}

# 판다스 Series() 함수로 dictionary를 Series로 변환, 변수 sr에 저장
sr= pd.Series(dict_data)

# sr의 자료형 출력
print(type(sr))
print('\n')
print(sr)
# %%
# -*- coding: utf-8 -*-

import pandas as pd

# 리스트를 시리즈로 변환하여 변수 sr에 저장
list_data = ['2019-01-01', 3.14, 'ABC', 100, True]
sr = pd.Series(list_data)
print(sr)
# %%
idx = sr.index
val = sr.values

print(idx)
print('\n')
print(val)
# %%
# -*- coding: utf-8 -*-

import pandas as pd

# 튜플을 시리즈로 변환 ( 인덱스 옵션 지정)
tup_data = ('영인', '2010-05-01', '여', True)
sr = pd.Series(tup_data, index=['이름','생년월일', '성별', '학생여부'])
print(sr)
# %%
# -*- coding: utf-8 -*-
print(sr[0])    # sr의 1번째 원소를 선택 (정수형 위치 인덱스)
print(sr['이름'])   # '이름' 라벨을 가진 원소를 선택 (인덱스 이름)

# %%
print(sr[[1,2]])
print('\n')
print(sr[['생년월일', '성별']])
# %%
### 여러 개의 원소를 선택
print(sr[1:2])
print('\n')
print(sr['생년월일' : '성별'])
# %%
# -*- coding: utf-8 -*-

import pandas as pd

# 열이름을 key로 하고, 리스트를 value로 갖는 딕셔너리 정의(2차원 배열)
dict_data = {'c0':[1,2,3], 'c1':[4,5,6], 'c2':[7,8,9], 'c3':[10,11,12], 'c4':[13,14,15]}

# 판다스 DataFrame() 함수로 딕셔너리를 데이터 프레임으로 변환. 변수 df에 저장
df = pd.DataFrame(dict_data)

# df의 자료형 출력
print(type(df))
print('\n')
# 변수 df에 저장되어 있는 데이터프레임 객체를 출력
print(df)
# %%
## 행 인덱스 / 열 이름 설정 : pandas.DataFrame( 2차원 배열
#                                          index=행 인덱스 배열,
#                                          columns=열 이름 배열 )
# -*- coding: utf-8 -*-

import pandas as pd

# 행 인덱스/열 이름 지졍하여 데이터 프레임 만들기
df = pd.DataFrame([[15, '남', '덕영중'], [17, '여', '수리중']],
                index=['준서', '예은'],
                columns=['나이', '성별', '학교'])

# 행 인덱스, 열 이름 확인하기
print(df)
print('\n')
print(df.index)
print('\n')
print(df.columns)
# %%

# 행 인덱스, 열 이름 변경하기
df.index = ['학생1', '학생2']
df.columns = ['연령', '남녀', '소속']

print(df)   # 데이터 프레임
print('\n')
print(df.index)
print('\n')
print(df.columns)
# %%
# -*- coding: utf-8 -*-

import pandas as pd

# 행 인덱스 / 열 이름 지정하여 데이터 프레임 만들기
df = pd.DataFrame([[15, '남', '덕영중'], [17, '여', '수리중']],
                    index=['준서', '예은'],
                    columns=['나이','성별', '학교'])

# 데이터프레임 df 출력
print(df)
print('\n')

# 열 이름 중, '나이'를 '연령'으로, '성별'을 '남녀'로, '학교'를 '소속'으로 바꾸기
df.rename(columns={'나이':'연령', '성별':'남녀', '학교':'소속'}, inplace=True)

# df의 행 인덱스 중에서, '준서'를 '학생1'로 '예은'을 '학생2'로 바꾸기
df.rename(index={'준서':'학생1', '예은':'학생2'}, inplace=True )

# df 출력(변경 후)
print(df)

# %%
# 행 삭제: DataFrame 객체.drop(행 인덱스 또는 배열, axis=0)
# 열 삭제: DataFrame 객체.drop(열 인덱스 또는 배열, axis=1)
# -*- coding: utf-8 -*-

import pandas as pd

# DataFrame() 함수로 데이터프레임 변환. 변수 df에 저장
exam_data = {'수학':[90, 80, 70], '영어':[98,89,95],
             '음악':[85, 95,100], '체육':[100, 90, 90]}

df = pd.DataFrame(exam_data, index=['서준', '우현', '인아'])
print(df)
print('\n')

# 데이터 프레임 df를 복제하여 변수 df2에 저장. df2의 1개 행(row) 삭제
df2 = df[:]
df2.drop('우현', inplace=True)
print(df2)
print('\n')

# 데이터 프레임 df를 복제하여 변수 df3에 저장. df3의 2개 행(row)삭제
df3 = df[:]
df3.drop(['우현','인아'], axis=0, inplace=True)
print(df3)
print('\n')

# %%
# -*- coding: utf-8 -*-

import pandas as pd

# DataFrame() 함수로 데이터프렝림 변환, 변수 df에 저장.
exam_data = {'수학':[90,80,70], '영어':[98,89,95],
             '음악':[85,95, 100], '체육':[100, 90,90]}

df = pd.DataFrame(exam_data, index=['서준', '우현', '인아'])
print(df)
print('\n')

# 데이터프레임 df를 복제하여 df4에 저장. df4의 1개 열(columns) 삭제
df4 = df[:]
df4.drop('수학', axis=1, inplace=True)
print(df4)
print('\n')

# 데이터프레임 df를 복제하여 df5에 저장. df5의 2개 열(columns)을 삭제
df5 = df[:]
df5.drop(['영어', '음악'], axis=1, inplace=True)
print(df5)
# %%
# 행 선택 : loc, iloc 인덱서를 사용!
# -*- coding: utf-8 -*-

import pandas as pd

# DataFrame() 함수로 데이터프레임 변환. 변수 df에 저장.
exam_data = {'수학':[90,80,70], '영어':[98,89,95],
             '음악':[85, 95, 100], '체육':[100, 90, 80]}

df = pd.DataFrame(exam_data, index=['서준', '우현', '인아'])
print(df)
print('\n')

# 행 인덱스를 사용하여 행 1개 선택
label1 = df.loc['서준']
position1 = df.iloc[0]
print(label1)
print('\n')
print(position1)
# %%
# 행 인덱스를 사용하여 2개 이상의 행 선택
label2 = df.loc[['서준','우현']]
position2 = df.iloc[[0,1]]
print(label2)
print('\n')
print(position2)

# %%
# 행 인덱스의 범위를 지정하여 행 선택
label3 = df.loc['서준': '우현']
position3= df.iloc[0:1]
print(label3)
print('\n')
print(position3)
# %%
# -*- coding: utf-8 -*-

import pandas as pd

# DataFrame() 함수로 데이터프레임 변환 변수 df에 저장
exam_data = {'이름' : ['서준', '우현', '인아'],
             '수학' : [90, 80, 70],
             '영어' : [98,89, 95],
             '음악' : [85, 95, 100],
             '체육' : [100, 90, 90]}
df = pd.DataFrame(exam_data)
print(df)

print(type(df))
print('\n')

# '수학' 정수 데이터만 선택, 변수 math1에 저장
math1 = df['수학']
print(math1)
print(type(math1))
print('\n')

# '영어' 점수 데이터만 선택. 변수 english에 저장
english = df['영어']
print(english)
print(type(english))
# %%
# '음악', '체육' 점수 데이터를 선택, 변수 music_gym에 저장
music_gym = df[['음악', '체육']]
print(music_gym)
print(type(music_gym))
print('\n')

# '수학' 점수 데이터만 선택, 변수 math2에 저장
math2 = df[['수학']]
print(math2)
print(type(math2))
# %%
# -*- coding: utf-8 -*-

import pandas as pd

# DataFrame() 함수로 데이터프레임 변환, 변수 df에 저장
exam_data = {'이름' : ['서준', '우현', '인아'],
             '수학' : [90,80,70],
             '영어' : [98,89, 95],
             '음악' : [85, 95, 100],
             '체육' : [100, 95, 90]}

df = pd.DataFrame(exam_data)

# '이름' 열을 새로운 인덱스로 지정하고 df 객체에 변경사항을 반영
df.set_index('이름', inplace=True)
print(df)
# %%
# 데이터프레임 df의 특정 원소 1개 선택('서준'의 '음악' 점수)
a = df.loc['서준', '음악']
print(a)
b = df.iloc[0,2]
print(b)
# %%
# 데이터프레임 df의 특정 원소 2개 이상 선택('서준'의 음악', '체육' 점수)
c = df.loc['서준', ['음악', '체육']]
print(c)
d = df.iloc[0,[2,3]]
print(d)
e = df.loc['서준', '음악':'체육']
print(e)
f = df.iloc[0, 2:]
print(f)
# %%
# df 2개 이상의 행과 열에 속하는 원소들 선택('서준', '우현'의 '음악', '체육' 점수)
g = df.loc[['서준','우현'], ['음악','체육']]
print(g)
h = df.iloc[[0,1],[2,3]]
print(h)
i = df.loc['서준':'우현', '음악':'체육']
print(i)
j = df.iloc[0:2, 2:]
print(j)
# %%
# -*- coding: utf-8 -*-

import pandas as pd

# DataFrame() 함수로 데이터프레임 변환. 변수 df에 저장
exam_data = {'이름' : ['서준', '우현', '인아'],
             '수학' : [90, 80, 70],
             '영어' : [98, 89, 95],
             '음악' : [85, 95, 100],
             '체육' : [100, 90, 90]}

df = pd.DataFrame(exam_data)
print(df)
print('\n')

# 데이터프레임 df에 '국어' 점수 열(columns) 추가. 데이터 값음 80 지정
df['국어'] = 80
print(df)
# %%
# -*- coding: utf-8 -*-

import pandas as pd

# DataFrame() 함수로 데이터프레임 변횐. 변수 df 에 저장
exam_data = {'이름' : ['서준', '우현', '안아'],
             '수학' : [90, 80, 70],
             '영어' : [98,89, 95],
             '음악' : [85, 95, 100],
             '체육' : [100, 90, 80]}

df = pd.DataFrame(exam_data)
print(df)
print('\n')

# 새로운 행(row) 추가 - 같은 원소 값 입력
df.loc[3] = 0
print(df)
print('\n')

# 새로운 행(row) 추가 - 원소 값 여러 개의 배열
df.loc[4] = ['동규', 90,80,70,60]
print(df)
print('\n')

# 새로운 행(row) 추가 - 기존 행 복사
df.loc['행5'] = df.loc[3]
print(df)
# %%
# 원소 값 변경
# -*- coding: utf-8 -*-

import pandas as pd

# DataFrame() 함수로 데이터프레임 변횐. 변수 df에 저장
exam_data = {'이름' : ['서준', '우현', '인아'],
             '수학' : [90, 80, 70],
             '영어' : [98,89,95],
             '음악' : [85, 95 ,100],
             '체육' : [100, 90, 90]}

df = pd.DataFrame(exam_data)
print(df)
print('\n')

# '이름' 열을 새올운 인덱스로 지정하고, df 객체에 변경사항을 변경
df.set_index('이름', inplace=True)
print(df)
print('\n')

# 데이터프레임 df의 특정 원소를 변경하는 방법: '서준'의 '체육' 점수
df.iloc[0][3] = 80
print(df)
print('\n')

df.loc['서준']['체육'] = 90
print(df)
print('\n')

df.loc['서준', '체육'] = 100
print(df)
# %%
# 데이터프레임 df의 원소 여러 개를 변경하는 방법: '서준'의 '음악', '체육' 점수
df.loc['서준', ['음악', '체육']] = 50
print(df)
print('\n')

df.loc['서준', ['음악', '체육']] = 100, 50
print(df)
# %%
# 행, 열 위치 바꾸기 : DataFrame 객체.transpose() 또는 DataFrame.T
# -*- coding: utf-8 -*-

import pandas as pd

# DataFrame() 함수로 데이터프레임 변환. 변수 df에 저장
exam_data = {'이름' : ['서준', '우현', '인아'],
             '수학' : [90, 80, 70],
             '엉어' : [98, 89, 95],
             '음악' : [85, 95, 100],
             '체육' : [100, 90, 90]}
df = pd.DataFrame(exam_data)
print(df)
print('\n')

# 데이터프레임 df를 전치하기(메소드 활용)
df = df.transpose()
print(df)
print('\n')

# 데이터프레임 df를 전치하기(클래스 속성 활용)
df = df.T
print(df)
# %%
