N = str(input())
data = [[2,1], [2,-1], [-2, 1], [-2, -1], [1,2], [1,-2], [-1,2], [-1, -2]]

x, y = 1, 1
cnt = 0
x, y = int(N[1]), int(ord(N[0]) -ord('a')) + 1
for dx,dy in data:
    if 1 <= x+dx <= 8 and 1 <= y+dy <= 8:
        cnt += 1

print(cnt)
