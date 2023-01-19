## 1. Pacific Atlantic Water Flow

### 🔮 My solution

- 첫번째로 시도한 코드는 dfs 방식

```python
def pacificAtlantic(self, heights):
    m, n = len(heights), len(heights[0])
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    def dfs(x, y, flow):
        for i in range(4):
            nx = x + dx[i]  # 다음 데이터를 찾기 위해 x는 양옆으로 움직일 수 있음
            ny = y + dy[i]  # y는 위아래로 움직일 수 있음

            if nx < 0 or ny < 0 or nx >= m or ny >= n:  # 범위를 벗어나는 경우
                continue
            if (nx, ny) not in flow:  # 인접한 데이터가 flow 에 없으면
                if heights[nx][ny] >= heights[x][y]:  # nx,ny가 x,y 이상이어야 이전 데이터로 '흐를' 수 있음
                    flow.add((nx, ny))  # 데이터 추가
                    dfs(nx, ny, flow)  # 인접 데이터를 시작 데이터로 재귀 호출

    p = set()
    a = set()

    for i in range(m):
        p.add((i, 0))  # 왼쪽
        a.add((i, n-1))  # 오른쪽
        dfs(i, 0, p)  # pacific 데이터들을 각각 dfs의 시작으로 넣어줌
        dfs(i, n - 1, a)  # atlantic 데이터들을 각각 dfs의 시작으로 넣어줌

    for i in range(n):
        p.add((0, i))  # 위
        a.add((m-1, i))  # 아래
        dfs(0, i, p)
        dfs(m - 1, i, a)

    return list(p&a)  # 둘의 교집합을 반환
```

### 🦦 Optimization (other solutions)

- 재귀 방식의 dfs 말고도 stack을 사용한 dfs나 queue를 사용한 bfs를 구현할 수 있음
  - 재귀보다 좀 더 빠른 런타임의 bfs

      ```python
      def pacificAtlantic(self, heights):
          m, n = len(heights), len(heights[0])
          dx = [-1, 1, 0, 0]
          dy = [0, 0, -1, 1]

          p = deque()
          a = deque()
          pacific = [[0] * n for _ in range(m)]
          atlantic = [[0] * n for _ in range(m)]

          res = []

          def bfs(heights, queue, flow):
              while queue:
                  x, y = queue.popleft()

                  for i in range(4):
                      nx = x + dx[i]
                      ny = y + dy[i]
                      if nx < 0 or ny < 0 or nx >= m or ny >= n:
                          continue
                      if flow[nx][ny] == 1:
                          continue 
                      if heights[nx][ny] >= heights[x][y]: 
                          queue.append([nx, ny]) 
                          flow[nx][ny] = 1
              return flow

          for i in range(m): 
              p.append([i, 0])
              a.append([i, n-1])
              pacific[i][0] = 1 
              atlantic[i][n-1] = 1 

          for i in range(n): 
              p.append([0, i])
              a.append([m-1, i])
              pacific[0][i] = 1 
              atlantic[m-1][i] = 1 

          pacific = bfs(heights, p, pacific)
          atlantic = bfs(heights, a, atlantic)

          for i in range(m): 
              for j in range(n): 
                  if pacific[i][j] + atlantic[i][j] == 2:
                      res.append([i, j])  

          return res
      ```

### 👊 문제 회고

그래프 문제는 어떤 알고리즘을 쓸지 감이 잘 잡히지만 이를 적용하는 것이 어렵다.. 
특히 개인적으로 dfs의 재귀 방식보다도 visited를 저장해 queue/stack 사용하는 방식이 구현하기 어려운 것 같다.
연습하자!!

## 2. Set Matrix Zeroes

### 🔮 My solution

- 시간복잡도 O(MN)
- 공간복잡도 O(M+N)

```python
def setZeroes(self, matrix):
    row, col = set(), set()
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if matrix[i][j] == 0:
                row.add(i)
                col.add(j)

    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if i in row or j in col:
                matrix[i][j] = 0
    return matrix
```

### 🦦 Optimization (other solutions)

- 아래와 같은 [코드](https://leetcode.com/problems/set-matrix-zeroes/solutions/177436/set-matrix-zeroes/) 를 사용하면 공간복잡도를 최적화할 수 있다고 한다
  - 시간복잡도 O(MN)
  - 공간복잡도 O(1)

```python
def setZeroes(self, matrix):
    is_col = False
    R = len(matrix)
    C = len(matrix[0])
    for i in range(R):
        if matrix[i][0] == 0:
            is_col = True
        for j in range(1, C):
            # If an element is zero, we set the first element of the corresponding row and column to 0
            if matrix[i][j]  == 0:
                matrix[0][j] = 0
                matrix[i][0] = 0

    # Iterate over the array once again and using the first row and first column, update the elements.
    for i in range(1, R):
        for j in range(1, C):
            if not matrix[i][0] or not matrix[0][j]:
                matrix[i][j] = 0

    # See if the first row needs to be set to zero as well
    if matrix[0][0] == 0:
        for j in range(C):
            matrix[0][j] = 0

    # See if the first column needs to be set to zero as well        
    if is_col:
        for i in range(R):
            matrix[i][0] = 0
```

### 👊 문제 회고

시간복잡도를 생각하는 것도 어려워서 공간복잡도를 잘 생각해보지 않았는데 이 문제의 2nd 솔루션을 찾아보면서
공간복잡도의 최적화도 필요하다는 점을 상기할 수 있었다. 
