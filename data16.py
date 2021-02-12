# %%
import pandas as pd
from pandas.core.indexes import period

# row와 columns값을 헤더값과 나라이름으로 해주기 위한 설정
df = pd.read_html('https://en.wikipedia.org/wiki/All-time_Olympic_Games_medal_table', header=0, index_col=0)
df[1]
# %%
# 전체 데이터 중에서 앞에서부터 5개까지의 데이터를 슬라이싱
summer = df[1].iloc[:,:5]
summer
# %%
# 컬럼명이 정확하지 않기 때문에 새롭게 지정해주기 위한 정의
summer.columns = ['경기수', '금', '은', '동', '계']
summer
# %%
# 금메달 순으로 내림차순으로 정렬된 데이터 
summer.sort_values('금', ascending=False)
# %%
# 액셀파일로 저장하기
summer.to_excel('하계올림픽메달.xlsx')
# %%
### 데이터 프레임 기초
import pandas as pd

index = pd.date_range('1/1/2000', periods=8)
print(index)
# %%
import numpy as np

df = pd.DataFrame(np.random.rand(8,3), index=index, columns=list('ABC'))
df
# %%
import numpy as np
import pandas as pd

index = pd.date_range('1/1/2000', periods=8)
df = pd.DataFrame(np.random.rand(8,3), index=index, columns=list('ABC'))
print(df['B'])
# %%
### numpy의 mask기능을 pandas에 적용하기
import numpy as np
import pandas as pd

index = pd.date_range('1/1/2000', periods=8)
df = pd.DataFrame(np.random.rand(8,3), index=index, columns=list('ABC'))
print(df['B'] > .4)
# %%
df2 = df[df['B'] > .4]
df2
# %%
# 2차원 배열 형태의 데이터 프레임 연산
# pandas에서는 기본적으로 행방향 축으로 계산을 한다.
# 경우에 따라서 열방향 축으로 계산하기도 합니다.
# axis=0은 행 방향을 나타내며 0이 기본값입니다.
# 열 방향에 데이터를 추가하기 위해 axis=1로 하면 됩니다.
df['E'] =np.sum(df, axis=1)
df
# %%
# 행 방향 축을 기준으로 한 연산
import pandas as pd
import numpy as np

index = pd.date_range('1/1/2000', periods=8)
df = pd.DataFrame(np.random.rand(8,3), index=index, columns=list('ABC'))
df['D'] = df['A'] / df['B'] # A열 값을 B열 값으로 나눈 값을 D열에 생성된다.
df
# %%
import pandas as pd
import numpy as np

index = pd.date_range('1/1/2000', periods=8)
df = pd.DataFrame(np.random.rand(8,3), index=index, columns=list('ABC'))
df['D'] = df['A'] / df['B']
# 행 우선 계산 값을 E에 저장
df['E'] = np.sum(df, axis=1)
df.head()
# %%
# 열 우선 계산을 하는 방법, 여러개의 열에 대한 계산을 하기 위해
# pandas 라이브러리를 사용해야 함.
# A열을 기준으로 데이터의 뺄셈이 이루어졌기 때문에
# A데이터는 0값이고, 나머지 데이터도 A만큼 뺸 값이 적용되었다.
import pandas as pd
import numpy as np

index = pd.date_range('1/1/2000', periods=8)
df = pd.DataFrame(np.random.rand(8,3), index=index,
columns=list('ABC'))
df['D'] = df['A'] / df['B']
df['E'] = np.sum(df, axis=1)
# A열의 데이터를 기준으로 열 우선 계산
df = df.sub(df['A'], axis=0)
df.head()
# %%
