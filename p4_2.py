# 8x8

# move 1 = >>I
# move 2 = II>
# abcdefgh = 97-104

# # main
# # my solution
# pos = str(input())
# ctr = 0

# # a1
# col = ord(pos[0]) - 96
# row = int(pos[1])

# # (1,1)

# m_n = [1,-1,1,-1,2,2,-2,-2]
# m_a = [2,2,-2,-2,1,-1,1,-1]

# for i in range(len(m_n)):
#     pos_col = col + m_n[i]
#     pos_row = row + m_a[i]
#     if (1 <= pos_col <= 8) and (1 <= pos_row <= 8):
#         ctr += 1
# print(ctr)


# solution

input_data = input()

row = int(input_data[1])
col = int(ord(input_data[0])) - int(ord('a')) + 1

steps = [(-2,-1), (-1,-2), (1,-2), (2,-1), (2,1), (1,2), (-1,2), (-2,1)]
ctr = 0

for step in steps:
    next_row = row + step[0]
    next_col = col + step[1]
    if (1 <= next_col <= 8) and (1 <= next_row <= 8):
        ctr += 1

print(ctr)