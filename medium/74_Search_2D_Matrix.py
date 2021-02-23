class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """

        n = len(matrix)
        if n == 0:
            return False
        
        m = len(matrix[0])
 
        if n == 1 and m==1 and matrix[0][0] != target:
            return False
        
        l = 0
        r = m*n-1
        while (l != r):
            mid = (l + r -1) >>1
            if matrix[mid/m][mid % m] < target:
                l = mid +1 
            else:
                r = mid
        return matrix[r/m][r % m] == target
