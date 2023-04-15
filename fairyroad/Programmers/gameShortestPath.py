from collections import deque

def solution(maps):
    dx = [0, 1, -1, 0]
    dy = [1, 0, 0, -1]
    queue = deque()
    queue.append((0,0))
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < len(maps) and 0 <= ny < len(maps[0]):
                if maps[nx][ny] == 1:
                    queue.append((nx, ny))
                    maps[nx][ny] = maps[x][y] + 1
    if maps[-1][-1] == 1:
        return -1
    else:
        return maps[-1][-1]
