from collections import deque

x, y = map(int, input().split())
graph = []
for i in range(x):
    graph.append(list(map(int,input().split())))    

dx = [1, 0]
dy = [0, 1]

queue = deque([(0,0)])
graph[0][0] = 1

while queue:
    tmp = list(queue.popleft())
    vx, vy = tmp[0], tmp[1]
    for z in range(2):
        nx, ny = vx + dx[z], vy+dy[z]
        if 0<=nx<x and 0<=ny<y and graph[nx][ny] != 0:
            graph[nx][ny] = max(graph[vx][vy]+1, graph[nx][ny])
            queue.append((nx,ny))

print(graph[x-1][y-1])
