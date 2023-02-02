class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:

        r = [-1, 0, 1, 0] # clockwise
        c = [0, 1, 0, -1]
        r_len = len(heights)
        c_len = len(heights[0])
    
        def check_flow(coord, visited): # O(n^2)
            while coord:
                x, y = coord.popleft()
                if (x, y) in visited: continue
                visited.add((x, y))
                for i in range(4):
                    nx, ny = x + r[i], y + c[i]
                    if r_len>nx>=0 and c_len>ny>=0 and (nx, ny) not in visited:
                        if heights[x][y] <= heights[nx][ny]:
                            coord.append((nx, ny))

        pacific_flow, visit_pacific = deque([(0, y) for y in range(c_len)] + [(x, 0) for x in range(r_len)]), set()
        atlantic_flow, visit_atlantic = deque([(r_len-1, x) for x in range(c_len)] + [(y, c_len-1) for y in range(r_len)]), set()

        check_flow(pacific_flow, visit_pacific) 
        check_flow(atlantic_flow, visit_atlantic)

        # total: O(n^2) ?
        return visit_pacific & visit_atlantic



'''
searched topic
- python  deque
- python set -> add
'''