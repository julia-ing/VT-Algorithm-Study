class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        m = len(grid) # 세로
        n = len(grid[0]) # 가로

        dq = deque()
        dq2 = deque()

        for i in range(0,m):
            for j in range(0,n):
                if grid[i][j]=="1":
                    dq.append((i, j)) # 세로, 가로

        dm = [0, 0, 1, -1] # 세로
        dn = [1, -1, 0, 0] # 가로

        visited = set()
        res = len(dq)
        not_unique = 0
        neighbor = set()
        while dq:
            if dq2:
                x, y = dq2.popleft()
            else:
                x, y = dq.popleft()
            if (x,y) in visited:
                continue
            if (x, y) not in neighbor:
                not_unique += 1
            
            for i in range(0,4):
                x2 = x + dm[i]
                y2 = y + dn[i]
                if 0<=x2<m and 0<=y2<n:
                    if grid[x2][y2]=="1" and (x2, y2):
                        dq2.append((x2, y2))
                        # if (x2, y2) not in neighbor:
                        neighbor.add((x2,y2))
                        visited.add((x,y))

        return not_unique
'''
# googling
deque

# 
느낀점: bfs로 풀다가 deque에 넣는 좌표의 순서에 따라서 오답과 정답이 달라지는 것을 보고 
general한 풀이가 아님을 느꼈다. 
이 문제는 dfs로 푸는 것이 더 적합한 것 같았다. ()방향상 섬의 끝까지 도달하고, 돌아와야 구석에 있는 1까지 셀 수 있었기 때문)
일단 bfs 풀고자 해서 다음과 같은 방법으로 풀었다.
    1. 8방위가 아닌 4방위만 사용한다.
        8방위까지하면, 실제로 이웃하는 땅이 아닌, 다른 섬의 땅까지 neighbor라고 인식할 수 있기 때문이다. 
    2. deque를 2개 사용한다.
        deque에서 POP되는 좌표의 순서가 중요한데, 첫번째 dq는 모든 1의 좌표를, 
        두번째 dq는 POP이 되는 순서가 bfs로 넣은 순서가 되도록 데이터를 유지한다.
이 방식대로 하니 47/49까지 성공하다가 time limit exceeded가 떴다! -> 아무래도 4방위만 쓴 탓이 크지 않았나 싶다.
코드를 다시 보니 data가 자료구조 안에 있는지 체크한 후 add하는 if문이 있길래 set으로 바꾸었더니 시간이 줄어 통과할 수 있었다.

참고자료: https://ssinee.tistory.com/entry/%EB%B0%B1%EC%A4%80-4963%EB%B2%88-%EC%84%AC%EC%9D%98-%EA%B0%9C%EC%88%98DFS-C
'''
