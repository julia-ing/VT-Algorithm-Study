N, M = map(int, input().split())
a, b, c = map(int, input().split())
data = []
for i in range(N):
    data.append(list(map(int, input().split())))

ori = "URDL"[c]
x, y = a, b
result = 0
cnt = 0
while True:
    print(ori, cnt, result)
    print("x and y", x,y)
    if ori == "U":
        ori = "L"
        if 1 <= y-1 <= M and data[x-1][y-2] != 1:
            y = y - 1
            cnt = 0
            data[x-1][y-2] = 1
        else:
            cnt += 1
    elif ori =="L":
        ori = "D"
        if 1 <= x + 1 <= M and data[x][y-1] != 1:
            x = x + 1
            cnt = 0
            data[x][y-1] = 1
        else:
            cnt += 1
    elif ori =="D":
        ori = "R"
        if 1 <= y + 1 <= M and data[x-1][y] != 1:
            y = y + 1
            cnt = 0
            data[x-1][y] = 1
        else:
            cnt += 1
    elif ori =="R":
        ori = "U"
        if 1 <= x - 1 <= M and data[x-2][y-1] != 1:
            x = x - 1
            cnt = 0
            data[x-2][y-1] = 1
        else:
            cnt += 1
    if cnt == 4:
        if ori == "U" and 1 <= y+1 <= M and data[x-1][y] != 1:
            y = y + 1
            data[x-1][y] = 1
        elif ori == "L" and 1 <= x-1 <= M and data[x-2][y-1] != 1:
            x = x - 1
            data[x-2][y-1] = 1
        elif ori == "D" and 1 <= x+1 <= M and data[x][y-1] != 1:
            x = x + 1
            data[x][y-1] = 1
        elif ori == "R" and 1 <= y-1 <= M and data[x-1][y-2] != 1:
            y = y - 1
            data[x-1][y-2] = 1
        else:
            break
    result += 1

print(result)
    
