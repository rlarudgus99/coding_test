import time
import numpy as np
from random import randint

s_t = time.time()

# main

a = []
for i in range(10):
    a.append(randint(1,10))

print(a)
print(np.sum(a))


e_t = time.time()

print('time : ', e_t - s_t)

