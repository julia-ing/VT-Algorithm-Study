'''
처음 작성한 코드가 좀 지저분해서 해당 코드는 solution을 많이 참고해서 작성한 최종 코드입니다.
일단 최종 코드 먼저 업로드하고, 처음 작성한 코드나 생각의 흐름 등은 다시 정리해서 올리도록 할게요! (시간관계상..)
'''

class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        row, col = [], []
        
        for r in range(len(matrix)):
            for c in range(len(matrix[0])):
                if matrix[r][c] == 0:
                    row.append(r)
                    col.append(c)
        
        for r in row:
            for i in range(len(matrix[0])):
                matrix[r][i] = 0
        
        for c in col:
            for i in range(len(matrix)):
                matrix[i][c] = 0
