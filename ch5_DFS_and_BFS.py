# Ch.5
# DFS / BFS


# stack
# 후입선출 구조
# pop() 을 이용해 마지막 원소를 삭제한다.


# stack = []

# stack.append(5)
# stack.append(2)
# stack.append(3)
# stack.append(7)

# stack.pop()

# stack.append(1)
# stack.append(4)

# stack.pop()

# print(stack)


# pop
# 선입선출 구조

# deque 라이브러리의 popleft() 메서드를 이용해 가장 처음 원소를 삭제한다.

# from collections import deque

# queue = deque()

# queue.append(5)
# queue.append(2)
# queue.append(3)
# queue.append(7)

# queue.popleft()

# queue.append(1)
# queue.append(4)
# queue.popleft()

# print(list(queue))


# 재귀함수
# recursive function
# 자기자신을 호출한다.
# 함수 선언 시, 자기 자신 함수를 호출하는 코드를 포함하도록 코딩
# 종결 조건이 없다면, 함수 호출을 무한대로 하게 되므로 일정 횟수 이상으로는 함수를 종결할 수 있도록 해야함

# def recursive_function(i):
#     if i == 100:
#         return print(i, '번째 재귀함수를 종료합니다.')
#     print(i, '번째 재귀함수에서', i+1,'번째 재귀함수를 호출합니다.')
#     recursive_function(i+1)

# recursive_function(1)


# factorial 예제

# def facto(n):
#     if n <= 1:
#         return 1
#     return n*(facto(n-1))

# print(facto(5))


# DFS ex

# def dfs(graph, v, visited):
#     visited[v] = True
#     print(v, end=' ')

#     for i in graph[v]:
#         if not visited[i]:
#             dfs(graph,i,visited)

# graph = [[],[2,3,8],[1,7],[1,4,5],[3,5],[3,4],[7],[2,6,8],[1,7]]
# visited = [False] * 9

# dfs(graph, 1, visited)


# BFS ex

from collections import deque

# def bfs(graph, start, visited):
#     queue = deque([start])
#     visited[start] = True
#     while queue:
#         v = queue.popleft()
#         print(v,end=' ')
#         for i in graph[v]:
#             if not visited[i]:
#                 queue.append(i)
#                 visited[i] = True

# graph = [[],[2,3,8],[1,7],[1,4,5],[3,5],[3,4],[7],[2,6,8],[1,7]]
# visited = [False] * 9

# bfs(graph, 1, visited)


