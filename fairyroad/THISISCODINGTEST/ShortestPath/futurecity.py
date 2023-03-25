# 다익스트라 알고리즘에는 2가지 방법이 있음
# priority queue보다 heapq가 더 빠르게 동작함
# priority queue는 우선순위가 가장 높은 데이터를 가장 먼저 삭제하는 특징이 있음
# 물건을 넣어서 가장 가치가 높은 것 부터 꺼내고 싶을 때 사용함

#플로이드 워셜로 풀 수 있음

n,m = map(int, input().split())
INF = int(1e9)
graph = [[INF]*(n+1) for _ in range(n+1)]

for a in range(1, n+1):
    for b in range(1, n+1):
        if a==b:
            graph[a][b] = 0

for _ in range(m):
    a,b = map(int, input().split())
    graph[a][b] = 1
    graph[b][a] = 1

x,k = map(int, input().split())

for k in range(1, n+1):
    for a in range(1, n+1):
        for b in range(1, n+1):
            graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])
            #바로 질러서 가는거랑, 거쳐서 올때 min값 기록

distance = graph[1][k] + graph[k][x]

if distance >= INF:
    print("-1")
else:
    print(distance)

