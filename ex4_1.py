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
print(ctr)
s_t = time.time()

end_pos_x = 1
end_pos_y = 1



while True:
    if ctr == 0:
        break

    for i in range(ctr):
        if direction[i] == 'R' :
            end_pos_x = end_pos_x
            end_pos_y = end_pos_y + 1
            if end_pos_y > n or end_pos_y < 0 or end_pos_x < 0 or end_pos_x > n:
                end_pos_x = end_pos_x
                end_pos_y = end_pos_y - 1

        elif direction[i] == 'L' :
            end_pos_x = end_pos_x
            end_pos_y = end_pos_y - 1
            if end_pos_y > n or end_pos_y < 0 or end_pos_x < 0 or end_pos_x > n:
                end_pos_x = end_pos_x
                end_pos_y = end_pos_y + 1
        
        elif direction[i] == 'U' :
            end_pos_x = end_pos_x - 1 
            end_pos_y = end_pos_y
            if end_pos_y > n or end_pos_y < 0 or end_pos_x < 0 or end_pos_x > n:
                end_pos_x = end_pos_x + 1 
                end_pos_y = end_pos_y
        
        else:
            end_pos_x = end_pos_x + 1 
            end_pos_y = end_pos_y
            if end_pos_y > n or end_pos_y < 0 or end_pos_x < 0 or end_pos_x > n:
                end_pos_x = end_pos_x - 1
                end_pos_y = end_pos_y        
        ctr -= 1

end_pos = [end_pos_x, end_pos_y]

print(end_pos)

e_t = time.time()



print('time : ', e_t - s_t)

