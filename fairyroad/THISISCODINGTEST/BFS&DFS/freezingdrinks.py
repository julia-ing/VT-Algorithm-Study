from collections import deque

x, y = map(int, input().split())
graph = []
for i in range(x):
    graph.append(list(map(int,input().split())))    

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
cnt = 0
queue = deque([])
for i in range(x):
    for j in range(y):
        if graph[i][j] == 0:
            queue.append((i,j))
            graph[i][j] = 1
            cnt += 1
            while queue:
                tmp = list(queue.popleft())
                vx, vy = tmp[0], tmp[1]
                for z in range(4):
                    nx, ny = vx + dx[z], vy+dy[z]
                    if 0<=nx<x and 0<=ny<y and graph[nx][ny] == 0:
                        graph[nx][ny] = 1
                        queue.append((nx,ny))
print(cnt)
