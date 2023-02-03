📝week5

✔number 1 : Number of islands

    bfs로 풀어야한다는 것까지 생각했는데, 1을 어떻게 처리할지에 대해서 생각하지 못했음
    아래의 링크를 참고함 : https://gamjatwigim.tistory.com/146
    1. 일단 처음의 1을 '-'와 같은 다른 문자로 바꿔주고 주변에 있는 1을 찾기 위해 bfs를 사용함
    2. 조건안에 포함이 되면 해당 1도 마찬가지 방법으로 bfs를 적용시킴
    3. 처음 1을 호출할 때만 cnt를 증가시키면 인접한 아이들을 1번씩만 증가시킬 수 있음
    
    class Solution(object):

    def bfs(self, grid, x, y):
        grid[x][y] = '-'
        dx = [1,0,-1,0]
        dy = [0,-1,0,1]
        if x < len(grid) - 1 and grid[x+1][y] == "1":
            self.bfs(grid, x+1, y)
        if x > 0 and grid[x-1][y] == "1":
            self.bfs(grid, x-1, y)
        if y > 0 and grid[x][y-1] == "1":
            self.bfs(grid, x, y-1)
        if y < len(grid[0]) - 1 and grid[x][y+1] == "1":
            self.bfs(grid, x, y+1)

    def numIslands(self, grid):
        cnt = 0
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == "1":
                    self.bfs(grid, i, j)
                    cnt = cnt + 1
        return cnt
        
![image](https://user-images.githubusercontent.com/74306759/216358927-4213bb07-a8bb-4fbd-9ee8-54873043dcb8.png)


✔number 2

        global: 일반함수 내에서 전역 변수를 사용할 때 사용하니까 nested function이 아니라 함수밖에 변수를 참조한다는 의미
        nonlocal : nested에서는 상위함수의 변수를 사용가능!
