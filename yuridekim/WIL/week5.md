### **Week 5**
|                                  #                                   |            TITLE             |        TAGS         |              DIFFICULTY               |
|:--------------------------------------------------------------------:|:----------------------------:|:-------------------:|:-------------------------------------:|
|      [200](https://leetcode.com/problems/number-of-islands/)      |      Number of Islands       |        Graph        | <span style="color:orange">Medium</span> |
| [124](https://leetcode.com/problems/binary-tree-maximum-path-sum/) | Binary Tree Maximum Path Sum |   Tree   |  <span style="color:red">Hard</span>  |

### 200. Number of Islands
#### 문제풀이
보자마자 처음에는 string을 reverse해서 dp로 풀어줘야하나라는 생각을 했지만 현재까지 가지고 있는 string이랑만 비교해주면 될 것 같아서 단순 string에서 window를 slide해주면서 풀어나가야겠다고 생각을 했다!

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
일단 string을 한자리씩 올라가면서 새로 들어오는 char를 넣어준다. 이때 고려해주는 점은 이미 갖고 있는 string에서 이미 들고 있는 char가 새로 들어오면 그 char가 들어오기 전까지의 원래 string의 길이를 비교해주고서 중복 char의 두번째 char개 시작하는 곳부터 string을 들고 있어준다.
예를 들어 wkpkefdtk 같은 경우 처음에는 wkp를 갖고 있다가 wkpk가 되는 순간 앞에 wk를 버리고 pk로 string을 교체해주고서 거기서부터 다시 string을 탐색해나간다!

- 생각해주지 못한 예외 처리들
> "au": 지금 코드 상으로 겹치는 char가 없으면 length를 측정해서 max로 교체해주는 시점이 없어서 추가해줬다.

> " ": length가 1인 경우도 따로 처리해줘야한다

> "cdd": 마찬가지로 cd에서 코드 때문에 d로 string을 교체해주기 전에 max length를 체크해주는 시점이 없어서 다음과 같이 매 iteration마다 그냥 max length를 체크해줬는데 이게 시간에 영향을 줬을 수도 있을 것 같다.


#### 💡 What I learned!
runtime: beats 87.87%
memory: beats 52.37%
처음에 문제를 보고 겁먹었지만 생각보다 쉬운 문제였지만 예외 처리를 많이 놓친 것 같다. 문제 조건을 꼼꼼히 읽어보자!
라이브 코테에서 이렇게 막무가내로 예외 상황을 생각 안 해주고 내버리면 혼날 것 같다!

```
if i<0 or j<0 or i>=len(grid) or j>=len(grid[0]) or grid[i][j]=='0' or grid[i][j]=='#' :
```

```
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # Base Case
        if len(s) == 1: return 1


        count, s_result = 0, ''

        for i in s:
            if i not in s_result:
                s_result += i
            else:
                s_result = s_result[s_result.index(i)+1:] + i

            if len(s_result) > count:
                count = len(s_result)
        
        return count
```
예시 코드랑 비교해보니 로직은 거의 비슷한 것 같은데 중복이 없을 경우에만 char를 더해준다는 점에서 차이를 가졌다. 나는 일단 더해주고 string에서 더해주기 전까지의 string이랑만 비교해줬는데 생각해보니 조금 비효율적이었던 것 같다!

-------------------------------------------------------------------
### 124. Binary Tree Maximum Path Sum
#### 문제풀이
처음에 감이 안 와서 topic이 dp인 것을 확인하고 어떤 걸 dp로 놓아야하나 고민하면서 첫 코드를 짰다.
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
첫 코드에서 바보같이 첫 occurence만 찾아서 대체해줘야했는데 replace 마지막에 1을 빼주는 걸 까먹어서 다시 넣어줬다. 답은 맞게 나왔는데 시간 복잡도가 beats 5.10%, memory가 beats 8.12%로 심각하게 나와서 어떻게 개선을 해줘야하나 고민해봤다.

그래서 list에 중복 string을 넣어주는 if 문을 빼면 매 case마다 if문을 측정하는 시간이 줄어들까?했지만 "aaaaaaaaaaaaaaaaaaaaaaaaaaaa"에서 메모리 부족이 떴다.



#### 💡 What I learned!
그래서 고민하다가 그냥 풀이를 참고했다.
```
def wordBreak(self, s, wordDict):
        dp = [False] * len(s)
        for i in range(len(s)):
            for w in wordDict:
                if w == s[i:i+len(w)] and (dp[i-1] or i == 0):
                    dp[i+(len(w)-1)] = True
        return dp[-1]
```
string의 길이만큼 array를 만들어주고 word로 짤려나간 마지막 index로부터 또 다시 word로 짤려나갈 수 있는지를 체크해주는 방식이었다. 이렇게 해당 char자리에 dp를 true로 설정해서 점점 오른쪽으로 탐색해나가는 방식이었다. 이런식으로 맨 마지막 char 자리도 true면 그 전 string까지 wordDict를 통해서 쪼갤 수 있는지 여부를 돌려준다.

확실히 memory면에 있어서 내 방식은 경우의 수에 따라 dp에 저장된 string의 숫자나 string의 길이도 변동이 심해서 상수로 거의 비슷한 공간을 차지하는 예시답안이 효율적일 것 같았다.
비슷한 로직인 것 같은데 time에서도 이렇게 많이 차이날 수 있다는 걸 깨달을 수 있는 문제였다.

...라고 생각했는데 submit해보니까 <b>틀린 답안</b>이라고 나온다! 백준 같은 경우는 플랫폼은 답안에서 배울 점이 많았는데 leetcode는 보면 vote를 많이 받은 submission이더라도 <i>엉터리인 경우도 많아서 조심해야한다.</i>

```
# Runtime Beats 94.62%
from collections import deque
class Solution:
    def wordBreak(self, s, wordDict):
        q = deque([s])
        seen = set() 
        while q:
            s = q.popleft()    # popleft() = BFS ; pop() = DFS
            for word in wordDict:
                if s.startswith(word):
                    new_s = s[len(word):]
                    if new_s == "": 
                        return True
                    if new_s not in seen:
                        q.append(new_s)
                        seen.add(new_s)
        return False
```
dp로 된 좋은 time complexity는 찾지 못했고 tree에서 좋은 예시답안을 찾았다.
또 string match에 있어서 일일히 index를 찾고, 제일 첫 occurence만 지정해줬는데 여기서 startswith이라는 좋은 기능을 사용하면 좋을 것 같다.
