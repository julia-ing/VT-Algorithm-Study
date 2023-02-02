# DFS using set()
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        n_island = 0
        n_row = len(grid)
        n_col = len(grid[0])
        visited = set()
        
        for i in range(n_row):
            for j in range(n_col):
                if grid[i][j]=='1' and not (i,j) in visited:
                    visited.add((i,j))
                    n_island += 1
                    l = [(i,j)]
                    
                    while l:
                        ii, jj = l.pop(0)
                        up, right, down, left = (ii-1,jj), (ii,jj+1), (ii+1,jj), (ii,jj-1)
                        if up[0]>=0 and grid[up[0]][up[1]]=='1' and not up in visited:
                            visited.add(up)
                            l.append(up)
                        if right[1]<n_col and grid[right[0]][right[1]]=='1' and not right in visited:
                            visited.add(right)
                            l.append(right)
                        if down[0]<n_row and grid[down[0]][down[1]]=='1' and not down in visited:
                            visited.add(down)
                            l.append(down)
                        if left[1]>=0 and grid[left[0]][left[1]]=='1' and not left in visited:
                            visited.add(left)
                            l.append(left)
        return n_island  
