๐week5

โnumber 1 : Number of islands

    bfs๋ก ํ์ด์ผํ๋ค๋ ๊ฒ๊น์ง ์๊ฐํ๋๋ฐ, 1์ ์ด๋ป๊ฒ ์ฒ๋ฆฌํ ์ง์ ๋ํด์ ์๊ฐํ์ง ๋ชปํ์
    ์๋์ ๋งํฌ๋ฅผ ์ฐธ๊ณ ํจ : https://gamjatwigim.tistory.com/146
    1. ์ผ๋จ ์ฒ์์ 1์ '-'์ ๊ฐ์ ๋ค๋ฅธ ๋ฌธ์๋ก ๋ฐ๊ฟ์ฃผ๊ณ  ์ฃผ๋ณ์ ์๋ 1์ ์ฐพ๊ธฐ ์ํด bfs๋ฅผ ์ฌ์ฉํจ
    2. ์กฐ๊ฑด์์ ํฌํจ์ด ๋๋ฉด ํด๋น 1๋ ๋ง์ฐฌ๊ฐ์ง ๋ฐฉ๋ฒ์ผ๋ก bfs๋ฅผ ์ ์ฉ์ํด
    3. ์ฒ์ 1์ ํธ์ถํ  ๋๋ง cnt๋ฅผ ์ฆ๊ฐ์ํค๋ฉด ์ธ์ ํ ์์ด๋ค์ 1๋ฒ์ฉ๋ง ์ฆ๊ฐ์ํฌ ์ ์์
    
    class Solution(object):

    def bfs(self, grid, x, y):
        grid[x][y] = '-'
        dx = [1,0,-1,0]
        dy = [0,-1,0,1]
        if x < len(grid) - 1 and grid[x+1][y] == "1":
            self.bfs(grid, x+1, y)
        if x > 0 and grid[x-1][y] == "1":
            self.bfs(grid, x-1, y)
        if y > 0 and grid[x][y-1] == "1":
            self.bfs(grid, x, y-1)
        if y < len(grid[0]) - 1 and grid[x][y+1] == "1":
            self.bfs(grid, x, y+1)

    def numIslands(self, grid):
        cnt = 0
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == "1":
                    self.bfs(grid, i, j)
                    cnt = cnt + 1
        return cnt
        
![image](https://user-images.githubusercontent.com/74306759/216358927-4213bb07-a8bb-4fbd-9ee8-54873043dcb8.png)


โnumber 2

        global: ์ผ๋ฐํจ์ ๋ด์์ ์ ์ญ ๋ณ์๋ฅผ ์ฌ์ฉํ  ๋ ์ฌ์ฉํ๋๊น nested function์ด ์๋๋ผ ํจ์๋ฐ์ ๋ณ์๋ฅผ ์ฐธ์กฐํ๋ค๋ ์๋ฏธ
        nonlocal : nested์์๋ ์์ํจ์์ ๋ณ์๋ฅผ ์ฌ์ฉ๊ฐ๋ฅ!
        
        class TreeNode:
            def __init__(self, val=0, left=None, right=None):
                self.val = val
                self.left = left
                self.right = right


        class Solution:
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
