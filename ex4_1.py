import time

# main

# R (0,1)
# L (0,-1)
# U (1,0)
# D (-1,0)

n = int(input())
direction = list(map(str, input().split()))

# direction [R L U R R]
# n = 5 (5 x 5)
# start_pos = (1,1)

ctr = len(direction)
ctr1 = ctr
# print(ctr)
s_t = time.time()

end_pos_x = 1
end_pos_y = 1



while True:
    if ctr1 == 0:
        break

    for i in range(ctr):
        if direction[i] == 'R' :
            end_pos_x = end_pos_x
            end_pos_y = end_pos_y + 1
            if end_pos_y > n or end_pos_y < 1 or end_pos_x < 1 or end_pos_x > n:
                end_pos_x = end_pos_x
                end_pos_y = end_pos_y - 1

        elif direction[i] == 'L' :
            end_pos_x = end_pos_x
            end_pos_y = end_pos_y - 1
            if end_pos_y > n or end_pos_y < 1 or end_pos_x < 1 or end_pos_x > n:
                end_pos_x = end_pos_x
                end_pos_y = end_pos_y + 1
        
        elif direction[i] == 'U' :
            end_pos_x = end_pos_x - 1 
            end_pos_y = end_pos_y
            if end_pos_y > n or end_pos_y < 1 or end_pos_x < 1 or end_pos_x > n:
                end_pos_x = end_pos_x + 1 
                end_pos_y = end_pos_y
        
        else:
            end_pos_x = end_pos_x + 1 
            end_pos_y = end_pos_y
            if end_pos_y > n or end_pos_y < 1 or end_pos_x < 1 or end_pos_x > n:
                end_pos_x = end_pos_x - 1
                end_pos_y = end_pos_y        
        ctr1 -= 1

end_pos = [end_pos_x, end_pos_y]

print(end_pos)

e_t = time.time()



print('time : ', e_t - s_t)


# # 2022-09-11
# # main

# n = int(input())
# plan = list(map(str, input().split()))

# if plan[0] == 'L':
#     print(plan[1])
# #        L R  U D
# d_row = [0,0,-1,1]
# d_col = [-1,1,0,0]

# p_row = 1
# p_col = 1

# ctr = 0

# def back_pos(cmd):
#     global p_row, p_col

#     if cmd == L:
#         p_row -= d_row[0]
#         p_col -= d_col[0]
#     elif cmd == R:
#         p_row -= d_row[1]
#         p_col -= d_col[1]
#     elif cmd == U:
#         p_row -= d_row[2]
#         p_col -= d_col[2]
#     elif cmd == D:
#         p_row -= d_row[3]
#         p_col -= d_col[3]
    
#     return p_row, p_col


# while True:
#     global L, R, U, D
#     for i in range(len(plan)):
#         if plan[i] == 'L':
#             p_row += d_row[0]
#             p_col += d_col[0]
#             if (1 > p_col) or (len(plan) < p_col) or (1 > p_row) or (len(plan) < p_row) :
#                 back_pos(L)

#         elif plan[i] == 'R':
#             p_row += d_row[1]
#             p_col += d_col[1]
#             if (1 > p_col) or (len(plan) < p_col) or (1 > p_row) or (len(plan) < p_row) :
#                 back_pos(R)

#         elif plan[i] == 'U':
#             p_row += d_row[2]
#             p_col += d_col[2]
#             if (1 > p_col) or (len(plan) < p_col) or (1 > p_row) or (len(plan) < p_row) :
#                 back_pos(U)

#         else:
#             p_row += d_row[3]
#             p_col += d_col[3]
#             if (1 > p_col) or (len(plan) < p_col) or (1 > p_row) or (len(plan) < p_row) :
#                 back_pos(D)

#         ctr += 1
#         if ctr > len(plan):
#             break

# print(p_row, p_col)