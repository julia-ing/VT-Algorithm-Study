## 1. Pacific Atlantic Water Flow

### ๐ฎ My solution

- ์ฒซ๋ฒ์งธ๋ก ์๋ํ ์ฝ๋๋ dfs ๋ฐฉ์

```python
def pacificAtlantic(self, heights):
    m, n = len(heights), len(heights[0])
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    def dfs(x, y, flow):
        for i in range(4):
            nx = x + dx[i]  # ๋ค์ ๋ฐ์ดํฐ๋ฅผ ์ฐพ๊ธฐ ์ํด x๋ ์์์ผ๋ก ์์ง์ผ ์ ์์
            ny = y + dy[i]  # y๋ ์์๋๋ก ์์ง์ผ ์ ์์

            if nx < 0 or ny < 0 or nx >= m or ny >= n:  # ๋ฒ์๋ฅผ ๋ฒ์ด๋๋ ๊ฒฝ์ฐ
                continue
            if (nx, ny) not in flow:  # ์ธ์ ํ ๋ฐ์ดํฐ๊ฐ flow ์ ์์ผ๋ฉด
                if heights[nx][ny] >= heights[x][y]:  # nx,ny๊ฐ x,y ์ด์์ด์ด์ผ ์ด์  ๋ฐ์ดํฐ๋ก 'ํ๋ฅผ' ์ ์์
                    flow.add((nx, ny))  # ๋ฐ์ดํฐ ์ถ๊ฐ
                    dfs(nx, ny, flow)  # ์ธ์  ๋ฐ์ดํฐ๋ฅผ ์์ ๋ฐ์ดํฐ๋ก ์ฌ๊ท ํธ์ถ

    p = set()
    a = set()

    for i in range(m):
        p.add((i, 0))  # ์ผ์ชฝ
        a.add((i, n-1))  # ์ค๋ฅธ์ชฝ
        dfs(i, 0, p)  # pacific ๋ฐ์ดํฐ๋ค์ ๊ฐ๊ฐ dfs์ ์์์ผ๋ก ๋ฃ์ด์ค
        dfs(i, n - 1, a)  # atlantic ๋ฐ์ดํฐ๋ค์ ๊ฐ๊ฐ dfs์ ์์์ผ๋ก ๋ฃ์ด์ค

    for i in range(n):
        p.add((0, i))  # ์
        a.add((m-1, i))  # ์๋
        dfs(0, i, p)
        dfs(m - 1, i, a)

    return list(p&a)  # ๋์ ๊ต์งํฉ์ ๋ฐํ
```

### ๐ฆฆ Optimization (other solutions)

- ์ฌ๊ท ๋ฐฉ์์ dfs ๋ง๊ณ ๋ stack์ ์ฌ์ฉํ dfs๋ queue๋ฅผ ์ฌ์ฉํ bfs๋ฅผ ๊ตฌํํ  ์ ์์
  - ์ฌ๊ท๋ณด๋ค ์ข ๋ ๋น ๋ฅธ ๋ฐํ์์ bfs

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

### ๐ ๋ฌธ์  ํ๊ณ 

๊ทธ๋ํ ๋ฌธ์ ๋ ์ด๋ค ์๊ณ ๋ฆฌ์ฆ์ ์ธ์ง ๊ฐ์ด ์ ์กํ์ง๋ง ์ด๋ฅผ ์ ์ฉํ๋ ๊ฒ์ด ์ด๋ ต๋ค.. 
ํนํ ๊ฐ์ธ์ ์ผ๋ก dfs์ ์ฌ๊ท ๋ฐฉ์๋ณด๋ค๋ visited๋ฅผ ์ ์ฅํด queue/stack ์ฌ์ฉํ๋ ๋ฐฉ์์ด ๊ตฌํํ๊ธฐ ์ด๋ ค์ด ๊ฒ ๊ฐ๋ค.
์ฐ์ตํ์!!

## 2. Set Matrix Zeroes

### ๐ฎ My solution

- ์๊ฐ๋ณต์ก๋ O(MN)
- ๊ณต๊ฐ๋ณต์ก๋ O(M+N)

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

### ๐ฆฆ Optimization (other solutions)

- ์๋์ ๊ฐ์ [์ฝ๋](https://leetcode.com/problems/set-matrix-zeroes/solutions/177436/set-matrix-zeroes/) ๋ฅผ ์ฌ์ฉํ๋ฉด ๊ณต๊ฐ๋ณต์ก๋๋ฅผ ์ต์ ํํ  ์ ์๋ค๊ณ  ํ๋ค
  - ์๊ฐ๋ณต์ก๋ O(MN)
  - ๊ณต๊ฐ๋ณต์ก๋ O(1)

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

### ๐ ๋ฌธ์  ํ๊ณ 

์๊ฐ๋ณต์ก๋๋ฅผ ์๊ฐํ๋ ๊ฒ๋ ์ด๋ ค์์ ๊ณต๊ฐ๋ณต์ก๋๋ฅผ ์ ์๊ฐํด๋ณด์ง ์์๋๋ฐ ์ด ๋ฌธ์ ์ 2nd ์๋ฃจ์์ ์ฐพ์๋ณด๋ฉด์
๊ณต๊ฐ๋ณต์ก๋์ ์ต์ ํ๋ ํ์ํ๋ค๋ ์ ์ ์๊ธฐํ  ์ ์์๋ค. 
