#다익스트라로 풀수있음
import heapq

n,m,c = map(int, input().split())
INF = int(1e9)

distance = [INF] * (n+1)
graph = [[] for _ in range(n+1)]

for _ in range(m):
    a,b,c = map(int, input().split())
    graph[a].append((b,c))

print(graph)
def dijkstra(start):
    q = []
    heapq.heappush(q,(0, start))
    distance[start] = 0
    while q:
        dist, now = heapq.heappop(q)
        if distance[now] < dist: #더하기도 전에 이미 작으면 패스
            continue
        for i in graph[now]:
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))

dijkstra(c)

result = 0
max_distance = 0

for i in range(1, n+1):
    if distance[i] != INF:
        result += 1
        max_distance = max(max_distance, distance[i])
print(result-1, max_distance)

print(distance)
