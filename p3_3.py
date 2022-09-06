import time
s_t = time.time()


# main
import random
import numpy as np

n,m = map(int, input().split())

res = 0

for i in range(n):
    data = list(map(int,input().split()))
    min_val = min(data)
    max_val = max(min_val, res)
    res = max_val
    print(res)

print('Final max_value is ', res)
e_t = time.time()
print('time : ', e_t - s_t)

