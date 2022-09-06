import time

s_t = time.time()


# # main
# # my solution

n, m, k = map(int, input().split())
data = list(map(int, input().split()))

data.sort()

first = data[n-1]
second = data[n-2]

hap_max = k*(m//k) * first
hap_max += second * (m - m//k * k)

print(hap_max)

# n = 5
# m = 7
# k = 2

# hap = 0

# aa = [3,4,3,4,3]

# max_aa = max(aa)
# hap_max = k * (m//k) * max_aa
# aa.remove(max_aa)

# max_aa = max(aa)
# hap_max += max_aa * (m - m//k * k)


# print(hap_max)


### solution

# n, m, k = map(int,input().split())
# data = list(map(int, input().split()))

# data.sort()
# first = data[n-1]
# second = data[n-2]

# res = 0

# while True:
#     for i in range(k):
#         if m == 0:
#             break
#         res += first
#         m -= 1
#     if m == 0:
#         break
#     res += second
#     m -= 1

# print(res)


# n, m, k = map(int, input().split())

# data = list(map(int, input().split()))

# data.sort()
# first = data[n-1]
# second = data[n-2]

# res = 0

# while True:
#     for i in range(k):
#         res += first
#         m -= 1
#         if m == 0:
#             break
#     res += second
#     m -= 1
#     if m == 0:
#         break
    
# print(res)

e_t = time.time()

print('solving time is ', e_t - s_t, '(s)')