### **Week 5**
|                                  #                                   |            TITLE             |        TAGS         |              DIFFICULTY               |
|:--------------------------------------------------------------------:|:----------------------------:|:-------------------:|:-------------------------------------:|
|      [200](https://leetcode.com/problems/number-of-islands/)      |      Number of Islands       |        Graph        | <span style="color:orange">Medium</span> |
| [124](https://leetcode.com/problems/binary-tree-maximum-path-sum/) | Binary Tree Maximum Path Sum |   Tree   |  <span style="color:red">Hard</span>  |

### 200. Number of Islands
#### 문제풀이
처음 로직은 island라면 어쨌든 동서남북 사방이 한번은 water일테니 4 방향을 한번이라도 접하게 되면 이를 true로 설정해주고 4개가 모두 true가 되면 island의 개수를 하나씩 늘려나가는 방법을 생각해봤다.

- First try
```
class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        island_direction=[]
        cur_island=0
        if any(grid)==1:
            island_direction.append([False, False, False, False])
        else:
            return 0
        m=len(grid); n=len(grid[0])

        for i in range(m):
            for j in range(n):
                if grid[i][j]=='1':
                    if not island_direction[cur_island][0]:
                        if j==0 or (j>0 and grid[i][j-1]=='0'):
                            island_direction[cur_island][0]=True
                    if not island_direction[cur_island][1]:
                        if i==0 or (i>0 and grid[i-1][j]=='0'):
                            island_direction[cur_island][1]=True
                    if not island_direction[cur_island][2]:
                        if j==(n-1) or (j<(n-1) and grid[i][j+1]=='0'):
                            island_direction[cur_island][2]=True
                    if not island_direction[cur_island][3]:
                        if i==(m-1) or (i<(m-1) and grid[i+1][j]=='0'):
                            island_direction[cur_island][3]=True
                    if all(island_direction[cur_island]):
                        cur_island+=1
                        island_direction.append([False, False, False, False])
        return cur_island
```
여기서 2/3 정도의 케이스가 통과했지만 [[1,1,1],[1,0,1],[1,1,1]]에서 패스를 못했다. [1][1]의 0을 만나기 전에 한번씩 사면 모두 물을 만나게 되지만 실제로 모두 이어져있기 때문에 2개가 아닌 1개의 island로 생각해줘야한다.


#### 💡 What I learned!
```
class Solution(object):
    def dfs(self, grid, i, j):
        if i<0 or j<0 or i>=len(grid) or j>=len(grid[0]) or grid[i][j]=='0' or grid[i][j]=='#' :
            return
        grid[i][j] = '#'
        self.dfs(grid, i-1, j)
        self.dfs(grid, i, j-1)
        self.dfs(grid, i+1, j)
        self.dfs(grid, i, j+1)

    def numIslands(self, grid):
        m=len(grid); n=len(grid[0])
        island_count=0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1':
                    self.dfs(grid, i, j)
                    island_count += 1
        return island_count
```
그래서 dfs를 이용해서 1을 만나면 사면을 탐색해주고 이를 visited로 표시해주기 위해 #으로 대체를 해준다. 그리고 탐색을 모두 완료하고 adjacent node에 더 이상 1이 없다면 island 개수를 늘려주는 방식으로 구현을 해줬다.

-------------------------------------------------------------------
### 124. Binary Tree Maximum Path Sum
#### 문제풀이
dp와 tree 문제가 혼용돼서 어려웠다.
```
class Solution(object):
    def dfs(self, node, dp):
        if not (node.left or node.right):
            return
        if not dp or (dp and dp[-1]<node.val):
            dp.append(node.val)

        #calculate left
        if node.left:
            path_sum=dp[-1]+node.left.val if dp[-1]>0 else node.left.val; dp.append(path_sum)
            self.dfs(node.left, dp)

        #calculate right
        if node.right:
            curr_max=max(dp)
            path_sum=curr_max+node.right.val if curr_max>0 else node.right.val; dp.append(path_sum)
            self.dfs(node.right, dp)
        
    def maxPathSum(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not (root.left or root.right):
            return root.val
        dp=list()
        self.dfs(root, dp)
        return max(dp)
```
첫 코드에서 시행착오를 겪은 게 여러번 코드를 수정해나갔지만 계속 예외 케이스들을 만나게 됐다.
left child를 탐색해나갈 때 0과의 max처리를 해주면 [-1,2]에서 에러가 나고 안 해주면 기본 제공된 케이스에서 또 에러가 났다.
대충 방향은 잡은 상태로 다시 풀이를 참고했다.

#### 💡 What I learned!
```
class Solution:
    def dfs(self, node):
        if not node: 
            return 0
        
        left_sum=self.dfs(node.left)
        if left_sum<0: left_sum=0
        right_sum=self.dfs(node.right)
        if right_sum<0: right_sum=0

        # max value of the path
        self.max_path = max(self.max_path, left_sum + right_sum + node.val)
        
        # add only one of the paths
        return max(left_sum, right_sum) + node.val
    def maxPathSum(self, root):
        self.max_path = float('-inf')
        self.dfs(root)
        return self.
```
문제를 풀면서 놓치고 있던 게 반드시 left나 right 중 하나를 선택해줘야한다는 것이다. 그래서 node가 있으면 먼저 left의 sum과 right의 sum을 구해준 다음에 자신에 해당하는 node value와 child에 해당하는 left와 right의 value들을 더해줘서 max sum을 구해준다. 처음 max sum 설정은 음수 input이 들어올 것까지 생각해 음의 infinity로 설정해준다.
