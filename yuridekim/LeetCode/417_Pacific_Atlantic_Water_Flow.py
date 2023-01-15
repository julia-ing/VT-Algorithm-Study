class Solution(object):
    def pacificAtlantic(self, heights):
        """
        :type heights: List[List[int]]
        :rtype: List[List[int]]
        """

        m=len(heights)
        n=len(heights[0])

        #nodes adjacent to ocean
        pacific  = [[0, i] for i in range(n)]   + [[i, 0] for i in range(1,m)]
        atlantic = [[m-1, i] for i in range(n)] + [[i, n-1] for i in range(m-1)]

        def bfs(ocean_nodes): 
            queue=ocean_nodes
            reached_ocean=list(ocean_nodes)
            reached_ocean.extend([item] for item in [[0,n-1],[m-1,0]] if item not in reached_ocean)

            while queue:          
                node = queue.pop(0) 
                x, y = node[0], node[1]

                for dx, dy in [(x, y+1), (x, y-1), (x-1, y), (x+1, y)]:
                    if 0<=dx and dx<m and 0<=dy and dy<n and heights[dx][dy]>=heights[x][y]:
                        if [dx,dy] not in reached_ocean:
                            reached_ocean.append([dx,dy])
                            queue.append([dx,dy])
            return reached_ocean
        reached_pacific=bfs(pacific)
        reached_atlantic=bfs(atlantic)
        return [inner for inner in reached_atlantic if inner in reached_pacific]