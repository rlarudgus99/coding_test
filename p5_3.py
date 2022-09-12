# solution


# row : n
# col : m

row, col = map(int,input().split())

graph = []
for i in range(row):
    graph.append(list(map(int,input())))

def dfs(pos_row, pos_col):

    if pos_row <= -1 or row <= pos_row or pos_col <= -1 or col <= pos_col:
        return False
    
    if graph[pos_row][pos_col] == 0 :
        graph[pos_row][pos_col] = 1
        dfs(pos_row - 1, pos_col)
        dfs(pos_row + 1, pos_col)
        dfs(pos_row, pos_col - 1)
        dfs(pos_row, pos_col + 1)
        return True
    return False


res = 0

for i in range(row):
    for j in range(col):
        if dfs(i,j) == True:
            res += 1
print(res)