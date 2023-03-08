N, M, K = map(int, input().split())
data = list(map(int, input().split()))

data.sort(reverse = True)
result = 0
cnt = 1
for i in range(M):
    if cnt <= K:
        result += data[0]
        cnt = cnt + 1
    else:
        result += data[1]
        cnt = 1
        i += 1
print(result)
