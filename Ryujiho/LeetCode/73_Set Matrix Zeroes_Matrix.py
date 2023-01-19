class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        M = len(matrix[0])
        zeroColumnsIdx = set()

        for i, itemList in enumerate(matrix):
            for j in range(M):
                if 0 == itemList[j]:
                    zeroColumnsIdx.add(j)
            if 0 in itemList:
                matrix[i] = [0]*M

        for i, itemList in enumerate(matrix):
            for idx in zeroColumnsIdx:
                matrix[i][idx] = 0