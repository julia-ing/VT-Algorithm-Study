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
