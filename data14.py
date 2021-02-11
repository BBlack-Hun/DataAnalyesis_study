#%%
import matplotlib.pyplot as plt
import numpy as np
from numpy.core.defchararray import replace

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
