#%%
from numpy import trim_zeros
import pandas as pd

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
             '음악':[85,95,]]}