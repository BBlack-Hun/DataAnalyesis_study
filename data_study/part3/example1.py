# %%
import pandas as pd

# read_csv() 함수로 df 생성
df = pd.read_csv('./auto-mpg.csv', header=None)
#df = df.drop(index=0, axis=0)

# 열 이름 지정
df.columns = ['mpg', 'cylinders', 'displacement', 'horsepower', 'weight',
              ' acceleration', 'model year', 'origin', 'name']
# 데이터프레임 df의 내용을 일부 확인
print(df.head())
print('\n')
print(df.tail())
# %%

# df의 모양과 크기 확인 : (행의 갯수, 열의 개수)를 튜플로 변환
print(df.shape)

# %%
print(df.info())
# %%

# 데이터 프레임 df의 자료형 확인
print(df.dtypes)
print('\n')

# 시리즈(mog 열)의 자료형 확인
print(df.mpg.dtypes)
# %%
