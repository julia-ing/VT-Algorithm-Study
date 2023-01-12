#My Solution
#0이 나오면 list_x, list_y에 0이 존재했던 위치를 넣어주고 나중에 list에서 하나씩 꺼내서 0으로 초기화시켜주는 것
class Solution(object):
    def setZeroes(self, matrix):
        r = len(matrix)
        c = len(matrix[0])
        list_x = []
        list_y = []
        for i in range(r):
            for j in range(c):
                if matrix[i][j] == 0:
                    list_x.append(i)
                    list_y.append(j)
        for i in range(len(list_x)):
            for a in range(c):
                matrix[list_x[i]][a] = 0
            for b in range(r):
                matrix[b][list_y[i]] = 0

                    
