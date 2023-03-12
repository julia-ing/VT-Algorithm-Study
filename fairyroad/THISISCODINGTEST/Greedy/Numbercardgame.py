N, M = map(int, input().split())
data = []
min_val = -1

for i in range(N):
    data.append(list(map(int, input().split())))
    min_val = max(min_val, min(data[i]))
print(min_val)
