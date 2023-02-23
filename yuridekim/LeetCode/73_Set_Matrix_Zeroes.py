class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        m = len(matrix)
        n = len(matrix[0])

        row_list=[]
        col_list=[]

        for i in range(m):
            for j in range(n):
                if matrix[i][j]==0:
                    if i not in row_list:
                        row_list.append(i)
                    if j not in col_list:
                        col_list.append(j)

        """ runtime beats 62%     
        for i in range(m):
            for j in range(n):
                if i in row_list or j in col_list:
                    matrix[i][j]=0"""
                    
        # runtime beats 96%
        for idx in row_list:
            for j in range(n):
                matrix[idx][j]=0
        
        for idx in col_list:
            for i in range(m):
                matrix[i][idx]=0