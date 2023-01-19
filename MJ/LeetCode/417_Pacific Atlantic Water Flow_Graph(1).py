# timeout solution
# 
class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:

        r = [-1, 0, 1, 0] # clockwise
        c = [0, 1, 0, -1]
        r_len = len(heights)
        c_len = len(heights[0])
        land = [ [0]*(c_len+2) for j in range(r_len+2)]
        for i in range(r_len):
            for j in range(c_len):
                land[i+1][j+1] = heights[i][j]

        def check_flow(r1, c1): # O(n^2)
            dir = [False for i in range(4)]
            visited = [[-1]*(c_len+2) for _ in range(r_len+2)]
            q=deque()
            q.append((r1,c1))
            
            while q:
                x, y = q.popleft()
                for i in range(4):
                    nx, ny = x + r[i], y + c[i]
                    if r_len+1>x>0 and c_len+1>y>0 and visited[nx][ny]==-1:
                        if land[x][y] >= land[nx][ny]:
                            q.append((nx, ny))
                            visited[nx][ny]=0
            
            if 0 in visited[0]:
                dir[0]=True
            for i in range(r_len+1):
                if visited[i][-1]==0:
                    dir[1]=True
                    break
            if 0 in visited[r_len+1]:
                dir[2]=True
            for i in range(r_len+1):
                if visited[i][0]==0:
                    dir[3]=True
                    break

            res = [False, False]
            if dir[0] or dir[3]:
                res[0] = True
            if dir[1] or dir[2]:
                res[1] = True
            
            return res[0] and res[1]

        result=[]
        for i in range(1, r_len+1):
            for j in range(1, c_len+1): # O(n^2)
                if check_flow(i, j): 
                    result.append([i-1, j-1])

        # total: O(n^4) ?
        return result



'''
searched topic
- python 2d array initialization
- (calss) function in functoin 
- reversed range
'''