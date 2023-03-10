## 1. Number of Islands

### ๐ฎ My solution

- dfs ๋ก ๋ชจ๋  ๋ฐฉํฅ์ ๋ํด ์ฌ๊ท ํธ์ถํด ๊ฐ๋ฉด์ ๋ฐฉ๋ฌธํ ๊ณณ์ ํ์ํด์ค๋ค. 
- ์๊ฐ ๋ณต์ก๋: O(M*N)

```python
def numIslands(self, grid):
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]

    row = len(grid)
    col = len(grid[0])
    res = 0

    def dfs(x, y):
        if x >= row or y >= col or x < 0 or y < 0 or grid[x][y] != '1':
            return
        grid[x][y] = '-'
        for i in range(4):
            dfs(x + dx[i], y + dy[i])

    for r in range(row):
        for c in range(col):
            if grid[r][c] == '1':
                dfs(r, c)
                res += 1
    return res
```

### ๐ ๋ฌธ์  ํ๊ณ 
- visited ๋ฅผ ์ฒ์์๋ ๋ฐฐ์ด๋ก ๋ฐ๋ก ๋ฌ์ ํ์์๋๋ฐ, ํ์ด๋ฅผ ์ฐธ๊ณ ํด๋ณด๋ 
์ด๋ฏธ ๋ฐฉ๋ฌธํ ๊ณณ์ '0' ๊ณผ '1' ์ด ์๋ ๋ค๋ฅธ ๋ฌธ์๋ก ๋์ฒดํ๋ ๋ฐฉ์์ ์ฌ์ฉํ๋๋ผ. ์ด๋ ๊ฒ ํ๋ฉด
๊ณต๊ฐ ํจ์จ์ฑ์ด ํจ์ฌ ์ข์์ง ๊ฒ ๊ฐ๋ค๋ ์๊ฐ์ด ๋ค์๋ค.

## 2. Binary Tree Maximum Path Sum

### ๐ฎ My solution

- ์ฒ์์๋ dp ๋ฐฉ์์ผ๋ก ํ์ด์ผํ๋ ๊ณ ๋ฏผํ๋๋ฐ ๋ง์ dp๋ฅผ ์ ์ฉํ๋ ค๋๊น ์ฝ๋๊ฐ ์ ์ง์ง์ง ์์์
์ฌ๊ท ๋ฐฉ์์ผ๋ก ์ด์ฌํ ํ์ด๋ดค๋ค.
- ์๋ก ์ ์ฌ์ค: **nonlocal vs. global** (์ฐธ๊ณ : [#](!https://devpouch.tistory.com/194))
  
  - ์๋ res ๋ณ์๋ฅผ ์ ์ญ์ผ๋ก ์ฌ์ฉํ๊ณ  ์ถ์ด์ global ํค์๋๋ฅผ ์ผ๋๋ฐ ์๋ฌ๊ฐ ๋ฌ๋ค. (NameError: name 'res' is not defined). ์ฐพ์๋ณด๋ nonlocal ํค์๋๊ฐ ๋ฐ๋ก ์์๋ค.
  - nonlocal: ์์ ํจ์์ ๋ณ์๋ฅผ ์ฐธ์กฐํ๋ค๊ณ  ๋ฏธ๋ฆฌ ์ ์ธ! ๋ฌธ์ ์์๋ search ํจ์ ๋ด์์ res ๋ณ์๋ฅผ nonlocal ๋ก ์ค์ ํด์ฃผ๋ฉด ์์ํจ์์ธ maxPathSum ์ res ๋ณ์๋ฅผ ์ฌ์ฉํ๊ฒ ๋จ.
  - global ๊ณผ์ ์ฐจ์ด: ์ ์ฉ ๋ฒ์
    
    - global ๋ณ์ : ์ผ๋ฐ ํจ์ ๋ด์์ ์ ์ญ ๋ณ์๋ฅผ ์ฌ์ฉํ  ๋ ์ฌ์ฉ (ํจ์ ์ธ๋ถ์ ๋ณ์๋ ์ ๊ทผ ๊ฐ๋ฅ)
    - nonlocal ๋ณ์ : ์ค์ฒฉ ํจ์ ๋ด์์ ์์ ํจ์์ ๋ณ์๋ฅผ ์ฌ์ฉํ  ๋ ์ฌ์ฉ

```python
def maxPathSum(self, root):
    def search(root):
        nonlocal res
        if not root:
            return 0
        leftSum = search(root.left)
        rightSum = search(root.right)
        res = max(res, leftSum + rightSum + root.val)
        return max(0, max(leftSum, rightSum) + root.val)

    res = float('-inf')
    search(root)
    return res
```

### ๐ฆฆ Optimization (other solutions)

- dp ์๋ฃจ์์ ์ฐพ์๋ณด์๋ค.

```python
class Solution(object):
    def maxPathSum(self, root):
        if root == None:
            return 0
        
        max_output = float("-inf")
        self.mem = {}
        
        que = [root]
        while que: #BFS
            node = que.pop()

            # DP optimization1
            if node in self.mem:
                max_output = max(self.mem[node], max_output)
            
            if node.left: 
                que.append(node.left)
            if node.right:
                que.append(node.right)
            
            # Consider including NO child, ONE child, BOTH children
            resultl = self.dfs(node.left) if node.left != None else 0
            resultr = self.dfs(node.right) if node.right != None else 0
            result = max(resultl, resultr, resultl + resultr)
            result = max(result + node.val, node.val)
            max_output = max(result, max_output)
        
        return max_output
        
    def dfs(self, node):
        # DP optimization2
        if node in self.mem:
            return self.mem[node]

        result = node.val
        resultl = float("-inf")
        resultr = float("-inf")

        if node.left:
            resultl = self.dfs(node.left)
        if node.right:
            resultr = self.dfs(node.right)

        # Consider including NO child OR ONE child
        max_result = max(result, result + max(resultl, resultr))

        self.mem[node] = max_result 

        return max_result
```

### ๐ ๋ฌธ์  ํ๊ณ 
์ฒ์์๋ dp ๋ฐฉ์์ผ๋ก ํ์ด์ผํ๋ ๊ณ ๋ฏผํ๋๋ฐ ๋ง์ dp๋ฅผ ์ ์ฉํ๋ ค๋๊น ์ฝ๋๊ฐ ์ ์ง์ง์ง ์์์
์ฌ๊ท ๋ฐฉ์์ผ๋ก ์ด์ฌํ ํ์ด๋ดค๋ค. ๋์๋ ์ด์จ๋  ํ์ด๋ฅผ ์ฐธ๊ณ ํ์ง๋ง ใใ 
