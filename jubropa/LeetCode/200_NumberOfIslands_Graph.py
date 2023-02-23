class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        height = len(grid)
        width = len(grid[0])

        offset = ((0,1),(0,-1),(1,0),(-1,0))

        result = 0

        stack = []

        for i in range(height):
            for j in range(width):
                if grid[i][j]=="0" or grid[i][j]=="#":
                    continue
                
                stack.append((i, j))
                while len(stack)!=0:
                    y, x = stack.pop()
                    grid[y][x]="#"
                    
                    for y_offset, x_offset in offset:
                        new_y = y - y_offset
                        new_x = x - x_offset
                        if (0 <= new_y < height) and (0 <= new_x < width):
                            if grid[new_y][new_x]=="1":
                                stack.append((new_y, new_x))
                result+=1
        
        return result
