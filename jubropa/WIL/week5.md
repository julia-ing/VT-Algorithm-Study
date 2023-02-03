## 200_Number of Islands_Graph

- 스택을 이용한 DFS입니다.
- 개인적으로 이런 식으로 DFS, BFS를 사용할 때는 '구덩이에 물을 붓는다'는 느낌으로 사용합니다. 이 문제를 예로 들면, "1"이 적힌 곳 만큼 구덩이가 파여있는 것이고, DFS를 수행하면서 "#"로 구덩이를 메워주는 것이고, 물을 부은 횟수가 정답이 되는 것입니다.


```python
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

```

## 124_Binary Tree Maximum Path Sum_Tree

- 보류...