# -*- coding: utf-8 -*-

n = 1260

# 500
c500 = n//500
n = n - c500*500

# 100
c100 = n//100
n = n - c100*100

# 50
c50 = n//50
n = n - c50*50

# 10
c10 = n//10
n = n - c10*10

print('c500 : ', c500)
print('c100 : ', c100)
print('c50 : ', c50)
print('c10 : ', c10)

print('coin  : ', c500+c100+c50+c10)


# n = 1260
# ctr = 0
# coin = 0
# hap = 0

# coin_types = [500,100,50,10]

# for i in coin_types:
#     coin = n // i
#     hap += coin
#     n = n - i * coin

# print(hap)