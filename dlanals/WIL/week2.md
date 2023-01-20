# 417. Pacific Atlantic Water Flow
- medium

## 의식의 흐름
- 먼저 하나하나 순회해봐야하나?
  - 시간 복잡도 : O(N^2)?
- recursion? 그럼 DP memorization방식 사용?
- 가장자리는 무조건 flow
- 가장자리가 아니면 좌우위아래 height 비교 -> 작거나 같은 칸이 없거나 가장자리일때까지 계속
  - 주변 순회는 어떻게?
  - 일단 짜본 코드
  ```python
  class Solution:
      def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
          m = len(heights)
          n = len(heights[0])
          flow = [['n' for j in range(n)] for i in range(m)]  # 리스트 초기화

          for i in range(m):
              for j in range(n):
                  # 가장자리는 무조건 flow
                  if i==0 or m-1:
                      flow[i][j] = 'y'

                  else:
                      if flow[i][j]=='y': break   # y로 memorization돼있을 때 루프 탈출
                      if heights[i][j] >= heights[i-1][j+1]:
                          i = i-1
                          j = j+1
                          # 여기까지 하다가 경우의 수가 너무 많아질듯하여 중단
  ```

## Solution

### DFS Recursion

- land->ocean으로 flow하는 것에서 생각을 전환하여 ocean->land로의 (반대 방향으로) flow를 생각해볼 수 있다.
- Recursive DFS는 코드의 가독성을 높여준다.
- 이전 cell보다 height가 높거나 같은 cell로 찾아가야한다.
- Pacific과 Atlantic 모두로부터 도달가능한 좌표를 추적하며 네 면에 대해 DFS를 수행한다.
- 두 좌표의 교차점을 찾자.


```python
# Recursive DFS
class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        m, n = len(heights), len(heights[0])
        
        def dfs(i: int, j: int, prev_height: int, coords: Set[Tuple[int]]) -> None:
            if i < 0 or i == m or j < 0 or j == n:
                # out of bounds
                return
            
            if (i, j) in coords:
                # already visited
                return
            
            height = heights[i][j]
            
            if height < prev_height:
                # water can't flow to a higher height
                return
            
            # ocean is reachable from current coordinate
            coords.add((i, j))
            
            # all four directions
            dfs(i + 1, j, height, coords)
            dfs(i - 1, j, height, coords)
            dfs(i, j + 1, height, coords)
            dfs(i, j - 1, height, coords)
            
        pacific_coords = set()
        
        # top row
        for j in range(n):
            dfs(0, j, 0, pacific_coords)
        
        # left col
        for i in range(m):
            dfs(i, 0, 0, pacific_coords)
            
        atlantic_coords = set()
            
        # right col
        for i in range(m):
            dfs(i, n - 1, 0, atlantic_coords)
            
        # bottom row
        for j in range(n):
            dfs(m - 1, j, 0, atlantic_coords)
            
        # intersection of coords reachable from both Pacific and Atlantic
        return list(pacific_coords & atlantic_coords)
```

### BFS
- 예원쌤 comment ) BFS가 런타임이 더 적게 나온다
- atlantic과 pacific에 대해 각각 BFS 수행해야 함
- 각 ocean으로부터 도달가능한 모든 행을 기록 (두 ocean으로부터 모두 도달 가능한 cell들은 정답의 일부)
- BFS는 현재 cell보다 높은 이웃 cell을 탐색한다. (반대 방향)

```python
class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        m, n = len(heights), len(heights[0])
        
        # visited
        atlantic_vis = [[False for _ in range(n)] for _ in range(m)]
        pacific_vis = [[False for _ in range(n)] for _ in range(m)]
        
        # double-ended queue (출입구가 양쪽에)
        atlantic = deque()
        pacific = deque()
        
        # 가장자리 4면 (두 ocean에 맞닿아있는 곳)
        for r in range(m):
            for c in range(n):
                if r == 0 or c == 0:
                    # 만약 pacific으로부터 방문했다면 pacific queue에 좌표 추가
                    # Q) 방문하지 않았어도 무조건 자표추가해야하는것 아닌가?
                    pacific_vis[r][c] = True
                    pacific.append((r, c))
                if r == m-1 or c == n-1:
                    atlantic_vis[r][c] = True
                    atlantic.append((r, c))
                    
        def bfs(queue, vis_mat):
            # 도달가능한 cell들 집합
            reach = set()
            
            while queue:
                # 맨 처음 cell의 좌표 pop
                r, c = queue.popleft()
                reach.add((r, c))

                # 주변 4개 cell 순회
                for nr, nc in [(r, c-1), (r, c+1), (r+1, c), (r-1, c)]:
                    
                    if not (0 <= nr < m and 0 <= nc < n): continue  # flow하지 않는 경우
                    if vis_mat[nr][nc]: continue    # 이미 방문한 경우

                    if heights[nr][nc] >= heights[r][c]:    # flow하는 경우
                        vis_mat[nr][nc] = True
                        queue.append((nr, nc))
            return reach
            
        
        # atlantic BFS
        atlantic_reach = bfs(atlantic, atlantic_vis)
        # pacific BFS
        pacific_reach = bfs(pacific, pacific_vis)
        
        return [[r, c] for r in range(m) for c in range(n) if (r,c) in pacific_reach and (r,c) in atlantic_reach]
            
```

## 느낀점
- 방향을 반대로 생각하는 방법은 미처 생각하지 못했는데, 다음부터는 잘 적용할 수 있도록 해보자.

