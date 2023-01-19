from collections import deque

#내가 푼거 아님..! 이 머리로는 bfs 써야 된다는 것 말고는 못알아냇움..ㅎ
#설명은 week2.md에 있습니당!
class Solution(object):
    def pacificAtlantic(self, heights):
        lenRow = len(heights)
        lenCol = len(heights[0])

        pacific = [[False for _ in range(lenCol)] for _ in range(lenRow)]
        atlantic = [[False for _ in range(lenCol)] for _ in range(lenRow)]

        dx = [1, -1, 0, 0]
        dy = [0, 0, 1, -1]

        pacificXY = deque()
        atlanticXY = deque()
        for i in range(lenRow):
            pacificXY.append([i, 0])
            atlanticXY.append([i, lenCol-1])
            for j in range(lenCol):
                pacificXY.append([0, j])
                atlanticXY.append([lenRow-1, j])

        # pacific
        visited = [[False for _ in range(lenCol)] for _ in range(lenRow)]
        while pacificXY:
            x, y = pacificXY.popleft()
            pacific[x][y] = True
            visited[x][y] = True
            for i in range(4):
                X = x + dx[i]
                Y = y + dy[i]
                if 0 <= X < lenRow and 0 <= Y < lenCol and not visited[X][Y] and heights[X][Y] >= heights[x][y]:
                    pacificXY.append([X,Y])
                    visited[x][y] = True

        # atlantic
        visited = [[False for _ in range(lenCol)] for _ in range(lenRow)]
        while atlanticXY:
            x, y = atlanticXY.popleft()
            atlantic[x][y] = True
            visited[x][y] = True
            for i in range(4):
                X = x + dx[i]
                Y = y + dy[i]
                if 0 <= X < lenRow and 0 <= Y < lenCol and not visited[X][Y] and heights[X][Y] >= heights[x][y]:
                    atlanticXY.append([X,Y])
                    visited[x][y] = True


        ans = []
        for i in range(lenRow):
            for j in range(lenCol):
                if pacific[i][j] and atlantic[i][j]:
                    ans.append([i, j])
        return ans
