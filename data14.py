#%%
import matplotlib.pyplot as plt
import numpy as np
from numpy.core.defchararray import replace
from numpy.lib.function_base import append

t = np.arange(0. , 5, .2)
plt.plot(t, t, 'r--', t, t**2, 'bs', t, t**3, 'g^')
plt.show()
# %%
import matplotlib.pyplot as plt

t = []
p2 = []
p3 = []

for i in range(0, 50, 2):
    t.append(i / 10)
    p2.append((i / 10) **2 )
    p3.append((i / 10) **3 )
plt.plot(t, t, 'r--', t, p2, 'bs', t, p3, 'g^')
plt.show()
# %%
import numpy as np
print(np.sqrt(2))
# %%
import numpy as np
print(np.pi)
print(np.sin(0))
print(np.cos(np.pi))

# %%
import numpy as np

a = np.random.rand(5)
print(a)
print(type(a))
# %%
import numpy as np

# 0~9까지의 숫자중 랜덤으로 10개의 숫자를 추출
print(np.random.choice(10, 10))
# %%
import numpy as np

# 0~9까지의 숫자중 6개를 뽑되 한번 뽑은 숫자는 재등장하지 않는다.
print(np.random.choice(10, 6, replace=False))
# %%
import numpy as np

# 0~5까지의 숫자 중 10개를 뽑되 다음과 같은 확률을 가진 체 뽑는다.
print(np.random.choice(6, 10, p=[.1,.1,.4,.2,.1,.1]))
# %%
import numpy as np
import matplotlib.pyplot as plt
dice = np.random.choice(6, 10)

plt.hist(dice, bins=6)
plt.show()
# %%
import numpy as np
import matplotlib.pyplot as plt

dice = np.random.choice(6, 1000000, p=[.1, .2, .3, .2, .1, .1])
plt.hist(dice, bins=6)
plt.show()
# %%
### numpy를 이용하여 Bubble 차트 그리기
import numpy as np
import matplotlib.pyplot as plt

x = np.random.randint(10, 100, 200)
y = np.random.randint(10, 100, 200)
size = np.random.randint(100)

plt.scatter(x, y, s=size, c=x, cmap='jet', alpha=.7)
plt.colorbar()
plt.show()
# %%
import numpy as np

a = np.array([1,2,3,4])
print(a)
# %%
import numpy as np
a = np.array([1,2,3,4])
print(a[1], a[-1])
print(a[1:])
# %%
import numpy as np
# array에 문자가 하나라도 존재하면 전제를 문자로 형변환하여 생성
a = np.array([1,2,'3',4])
print(a)
# %%
import numpy as np
# 파라미터로 받은 수만큼 0으로 채워진 배열 생성
a = np.zeros(10)
print(a)
# %%
import numpy as np
# 파라미터로 받은 수만큼 1로 채워진 배열 생성
a = np.ones(10)
print(a)
# %%
import numpy as np
# 파라미터로 받은 수만큼, 단위 배열을 생성 (대각선이 1로 채워진)
a = np.eye(3)
print(a)
# %%
import numpy as np
# 0~3까지의 배열 출력
print(np.arange(3))
# 3~6까지의 배열 출력
print(np.arange(3, 7))
# 3~6까지 2씩 띄어진 배열 출력 (|3|4|5|6|)
print(np.arange(3,7,2))
# %%
import numpy as np
# 1부터 2까지 0.1 간격으로 나눈다.
a = np.arange(1, 2, .1)
# 1부터 2까지 11개의 간격으로 나눈다.
b=  np.linspace(1,2, 11)
print(a)
print(b)
# %%
import numpy as np
a = np.arange(-np.pi, np.pi, np.pi/10)
b = np.linspace(-np.pi, np.pi, 20)
print(a)
print(b)
# %%
import numpy as np
a = np.zeros(10) + 5
print(a)
# %%
import numpy as np
a = np.linspace(1, 2, 11)
print(np.sqrt(a))
# %%
import numpy as np
import matplotlib.pyplot as plt

a = np.arange(-np.pi, np.pi, np.pi/100)
plt.plot(a, np.sin(a))
plt.show()
# %%
import numpy as np
import matplotlib.pyplot as plt

a = np.arange(-np.pi, np.pi, np.pi/100)
plt.plot(a, np.sin(a))
plt.plot(a, np.cos(a))
plt.plot(a+np.pi/2, np.sin(a))
plt.show()
# %%
import numpy as np
a = np.arange(-5, 5)
print(a)
# %%
print(a<0)
# %%
print(a[a<0])
# %%
mask1 = abs(a) > 3
print(a[mask1])
# %%
mask1 = abs(a) > 3
mask2 = abs(a) % 2 == 0
print(a[mask1 + mask2])
print(a[mask1*mask2])
# %%
import numpy as np
import matplotlib.pyplot as plt

x = np.random.randint(-100, 100, 1000)
y = np.random.randint(-100, 100, 1000)
# 이 부분이 책이랑 다름!!!! 이 부분이 책이랑 다름!!!! 이 부분이 책이랑 다름!!!!
size = np.random.randint(100)

mask1 = abs(x) > 50
mask2 = abs(y) > 50

x= x[mask1+mask2]
y= y[mask1+mask2]

plt.scatter(x, y, s=size, c=x, cmap='jet', alpha=.7)
plt.colorbar()
plt.show()
# %%
