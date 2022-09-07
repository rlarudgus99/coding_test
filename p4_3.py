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

# 처음 시작하는 위치 (x,y)
# 바라보는 방향 direction (위부터 시계방향 0 1 2 3)
x, y, direction = map(int, input().split())

# 처음 위치한 곳
# d[x][y] = 1 ?
# 한번 갔던 곳은 가면 안됨 == 바다 (1)
d[x][y] = 1

# 0으로 채워진 지도는 만들어졌음
# 실제 시뮬레이션에 사용될 지도를 만들기
array = []
for i in range(n):
    array.append(list(map(int,input().split())))

# 북 : 0
# 동 : 1
# 남 : 2
# 서 : 3

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

# 매뉴얼 1번
# 위치한 구역에서 바라보는 방향 기준 왼쪽으로 방향 전환
# 북쪽을 (0) 바라보는 경우, 왼쪽으로 틀면 서쪽(3)
def turn_left():
    global direction
    direction -= 1
    if direction == -1:
        direction = 3

# 시작하는 순간 방문 구역 1
ctr = 1
# 매번 캐릭터는 돌아야 함, 4법 돌았다 == 갈 곳이 없으므로 break
turn_time = 0


while True:
    turn_left()
    # turn_left() 하여 결정된 direction (0,1,2,3)에 맞는 인덱스만큼 이동
    nx = x + dx[direction]
    ny = y + dy[direction]
    
    # 현재 바라보고 있는 구역이 바다가 아닌 경우
    if d[nx][ny] == 0 and array[nx][ny] == 0:
        
        # 밟을 구역을 바다로 초기화
        d[nx][ny] = 1
        # 땅을 잘 밟았고, 밟고 있는 구역을 현재 내 위치로 저장
        x = nx
        y = ny
        ctr += 1
        turn_time = 0
        # while문을 반복할것 (다시 처음으로)
        continue
    else:
        # 한바퀴 씩 도는 것을 변수로 저장
        # turn_time + 1 -> turn_left()
        # turn_left 이후 바라보는 방향의 구역이 땅인 경우 if 문으로, turn_time 초기화
        # turn_left 이후 바라보는 방향의 구역이 바다인 경우 else 문, turn_time + 1
        turn_time += 1
    
    if turn_time == 4:
        # 한바퀴 돌았는데도 갈 곳이 없다
        # 뒤로 돌아가야함
        nx = x - dx[direction]
        ny = y - dy[direction]
        # 돌아갈 곳이 땅이면 돌아가기
        if array[nx][ny] == 0:
            x = nx
            y = ny
        else:
            # 돌아갈 곳이 땅이 아니면 break
            # simulation 끝
            break
        turn_time = 0
print(ctr)