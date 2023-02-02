## 1. Number of Islands

### 🔮 My solution

- dfs 로 모든 방향에 대해 재귀 호출해 가면서 방문한 곳은 표시해준다. 
- 시간 복잡도: O(M*N)

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

### 👊 문제 회고
- visited 를 처음에는 배열로 따로 둬서 풀었었는데, 풀이를 참고해보니 
이미 방문한 곳은 '0' 과 '1' 이 아닌 다른 문자로 대체하는 방식을 사용하더라. 이렇게 하면
공간 효율성이 훨씬 좋아질 것 같다는 생각이 들었다.

## 2. Binary Tree Maximum Path Sum

### 🔮 My solution

- 처음에는 dp 방식으로 풀어야하나 고민했는데 막상 dp를 적용하려니까 코드가 잘 짜지지 않아서
재귀 방식으로 열심히 풀어봤다.
- 새로 안 사실: **nonlocal vs. global** (참고: [#](!https://devpouch.tistory.com/194))
  
  - 원래 res 변수를 전역으로 사용하고 싶어서 global 키워드를 썼는데 에러가 났다. (NameError: name 'res' is not defined). 찾아보니 nonlocal 키워드가 따로 있었다.
  - nonlocal: 상위 함수에 변수를 참조한다고 미리 선언! 문제에서는 search 함수 내에서 res 변수를 nonlocal 로 설정해주면 상위함수인 maxPathSum 의 res 변수를 사용하게 됨.
  - global 과의 차이: 적용 범위
    
    - global 변수 : 일반 함수 내에서 전역 변수를 사용할 때 사용 (함수 외부의 변수는 접근 가능)
    - nonlocal 변수 : 중첩 함수 내에서 상위 함수의 변수를 사용할 떄 사용

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

### 🦦 Optimization (other solutions)

- dp 솔루션을 찾아보았다.

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

### 👊 문제 회고
처음에는 dp 방식으로 풀어야하나 고민했는데 막상 dp를 적용하려니까 코드가 잘 짜지지 않아서
재귀 방식으로 열심히 풀어봤다. 끝에는 어쨌든 풀이를 참고했지만 ㅜㅜ 
