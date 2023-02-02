class Solution(object):

  def numIslands(self, grid):
    output = 0

    # Find DFS (adjacent 1's - change to 0)
    dir = [(1, 0), (0, 1), (-1, 0), (0, -1)]

    def dfs(i, j):
      grid[i][j] = "0"

      for d in dir:
        ii, jj = i + d[0], j + d[1]

        if ii < 0 or jj < 0 or ii >= n or jj >= m: continue
        if grid[ii][jj] == "1":
          dfs(ii, jj)

    # Find 1 (island)
    n, m = len(grid), len(grid[0])
    for i in range(n):
      for j in range(m):
        if grid[i][j] == "1":
          output += 1
          dfs(i, j)

    return output


## We can add visited flag to not check visited place -> To decrease runtime speed
