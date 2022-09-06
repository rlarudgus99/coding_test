import time
s_t = time.time()

# main

n, k = map(int, input().split())
ctr = 0

while True:
    if n == 1:
        break
    if n%k == 0:
        n = n/k
        ctr +=1
    else:
        n -= 1
        ctr +=1

print(ctr)

e_t = time.time()
print('time : ', e_t - s_t)

