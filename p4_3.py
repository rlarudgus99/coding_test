# -*- coding: utf-8 -*-


### problem
# input :
# 4 4
# 1 1 0
# 1 1 1 1
# 1 0 0 1
# 1 1 0 1
# 1 1 1 1
# output :
# 4


# solution

n, m = map(int, input().split())

d = [[0] * m for _ in range(n)]

# ó�� �����ϴ� ��ġ (x,y)
# �ٶ󺸴� ���� direction (������ �ð���� 0 1 2 3)
x, y, direction = map(int, input().split())

# ó�� ��ġ�� ��
# d[x][y] = 1 ?
# �ѹ� ���� ���� ���� �ȵ� == �ٴ� (1)
d[x][y] = 1

# 0���� ä���� ������ ���������
# ���� �ùķ��̼ǿ� ���� ������ �����
array = []
for i in range(n):
    array.append(list(map(int,input().split())))

# �� : 0
# �� : 1
# �� : 2
# �� : 3

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

# �Ŵ��� 1��
# ��ġ�� �������� �ٶ󺸴� ���� ���� �������� ���� ��ȯ
# ������ (0) �ٶ󺸴� ���, �������� Ʋ�� ����(3)
def turn_left():
    global direction
    direction -= 1
    if direction == -1:
        direction = 3

# �����ϴ� ���� �湮 ���� 1
ctr = 1
# �Ź� ĳ���ʹ� ���ƾ� ��, 4�� ���Ҵ� == �� ���� �����Ƿ� break
turn_time = 0


while True:
    turn_left()
    # turn_left() �Ͽ� ������ direction (0,1,2,3)�� �´� �ε�����ŭ �̵�
    nx = x + dx[direction]
    ny = y + dy[direction]
    
    # ���� �ٶ󺸰� �ִ� ������ �ٴٰ� �ƴ� ���
    if d[nx][ny] == 0 and array[nx][ny] == 0:
        
        # ���� ������ �ٴٷ� �ʱ�ȭ
        d[nx][ny] = 1
        # ���� �� ��Ұ�, ��� �ִ� ������ ���� �� ��ġ�� ����
        x = nx
        y = ny
        ctr += 1
        turn_time = 0
        # while���� �ݺ��Ұ� (�ٽ� ó������)
        continue
    else:
        # �ѹ��� �� ���� ���� ������ ����
        # turn_time + 1 -> turn_left()
        # turn_left ���� �ٶ󺸴� ������ ������ ���� ��� if ������, turn_time �ʱ�ȭ
        # turn_left ���� �ٶ󺸴� ������ ������ �ٴ��� ��� else ��, turn_time + 1
        turn_time += 1
    
    if turn_time == 4:
        # �ѹ��� ���Ҵµ��� �� ���� ����
        # �ڷ� ���ư�����
        nx = x - dx[direction]
        ny = y - dy[direction]
        # ���ư� ���� ���̸� ���ư���
        if array[nx][ny] == 0:
            x = nx
            y = ny
        else:
            # ���ư� ���� ���� �ƴϸ� break
            # simulation ��
            break
        turn_time = 0
print(ctr)