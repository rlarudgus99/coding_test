# import time

# # main
# # my solution

# n = int(input())
# ctr = 0
# s_t = time.time()

# res = 0

# for m10 in range(6):
#         for m1 in range(10):
#             for s10 in range(6):
#                 for s1 in range(10):
#                     if (m10 == 3) or (m1 == 3) or (s10 == 3) or (s1 == 3):
#                         ctr += 1

# if n >= 3:
#     mtp = n
#     wgt = 3600
# elif n < 3 :
#     mtp = n+1
#     wgt = 0

# res = ctr * mtp + wgt

# e_t = time.time()

# print(res)
# print('\n')
# print('time : ',e_t - s_t,'s')


# solution

ctr = 0
n = int(input())

for i in range(n+1):
    for j in range(60):
        for k in range(60):
            if '3' in str(i) + str(j) + str(k):
                ctr += 1


print(ctr)