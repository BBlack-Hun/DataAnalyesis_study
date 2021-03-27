#%%
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
