class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        r = [-1, 0, 1, 0] # clockwise
        c = [0, 1, 0, -1]
        zero_coord = deque()

        len_x = len(matrix[0])
        len_y = len(matrix)

        for i in range(len_y): # get zero points # O(nm)
            for j in range(len_x):
                if matrix[i][j] == 0:
                    zero_coord.append((i, j))

        while zero_coord: # O(nm*(m+n)) ? -> O(n^3) ?
            y, x = zero_coord.popleft()
            for i in range(4): # clockwise 
                ny, nx = y + r[i], x + c[i]
                while True:
                    if 0<=nx<len_x and 0<=ny<len_y:
                        if matrix[ny][nx] != 0:
                            matrix[ny][nx] = 0
                        ny, nx = ny + r[i], nx + c[i]
                    else: break

        # space : O(nm) for zero_coord 
        # to be O(n+m), use coord for each row, column and then apply to matrix