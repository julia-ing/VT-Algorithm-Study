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




solution=Solution()
grid = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]
print(solution.numIslands(grid))