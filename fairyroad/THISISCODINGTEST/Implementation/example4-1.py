N = int(input())
data = map(str, input().split())

x, y = 1, 1

for i in data:
    if i == "D" and 0 < x + 1 < N :
        x = x + 1
    elif i =="U" and 0 < x-1 < N:
        x = x - 1
    elif i == "L" and 0 < y-1 < N:
        y = y - 1
    elif i == "R" and 0 < y+1 < N:
        y = y + 1

print(x, y)
