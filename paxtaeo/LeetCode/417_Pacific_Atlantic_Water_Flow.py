class Solution:
    def dfs(self, heights, r, c, visited):
        m, n = len(heights), len(heights[0])
        directions = ((0, 1), (0, -1), (1, 0), (-1, 0))

        visited[r][c] = True
        for d in directions:
            nr, nc = r+d[0], c+d[1]
            if nr < 0 or nr >= m or nc < 0 or nc >= n or visited[nr][nc] or heights[r][c] > heights[nr][nc]:
                continue
            self.dfs(heights, nr, nc, visited)

    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        if len(heights) == 0:
            return []
        
        m, n = len(heights), len(heights[0])
        visited_p = [[False for _ in range(n)] for _ in range(m)]
        visited_a = [[False for _ in range(n)] for _ in range(m)]

        for cr in range(m):
            self.dfs(heights, cr, 0, visited_p)
            self.dfs(heights, cr, n-1, visited_a)
        
        for cc in range(n):
            self.dfs(heights, 0, cc, visited_p)
            self.dfs(heights, m-1, cc, visited_a)

        ans = []
        for r in range(m):
            for c in range(n):
                if visited_p[r][c] and visited_a[r][c]:
                    ans.append([r, c])
        
        return ans