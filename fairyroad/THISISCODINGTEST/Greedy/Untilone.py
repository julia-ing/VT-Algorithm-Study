N, K = map(int, input().split())
cnt = 0
while N != 1:
    if K > 1 and N%K == 0:
        N = N // K
    else:
        N = N - 1
    cnt = cnt + 1
print(cnt)


#문제풀 때 N, K의 경우의 수를 적어보면서 수식을 만들어보았음!
