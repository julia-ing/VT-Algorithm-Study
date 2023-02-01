class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        
        self.m = len(heights)
        self.n = len(heights[0])
        self.heights = heights
        
        pacific_coords = set()

        for i in range(self.m):
            self.DFS(i, 0, 0, pacific_coords)
        for j in range(self.n):
            self.DFS(0, j, 0, pacific_coords)

        atlantic_coords = set()

        for i in range(self.m):
            self.DFS(i, self.n-1, 0, atlantic_coords)
        for j in range(self.n):
            self.DFS(self.m-1, j, 0, atlantic_coords)

        return sorted(list(pacific_coords & atlantic_coords))


    def DFS(self, i:int, j:int, prev_height:int, coords:set[tuple[int, int]]) -> None:

        if i==-1 or i==self.m or j==-1 or j==self.n:
            return

        if (i, j) in coords:
            return

        cur_height = self.heights[i][j]

        if cur_height < prev_height:
            return

        coords.add((i, j))

        self.DFS(i-1, j, cur_height, coords)
        self.DFS(i+1, j, cur_height, coords)
        self.DFS(i, j-1, cur_height, coords)
        self.DFS(i, j+1, cur_height, coords)