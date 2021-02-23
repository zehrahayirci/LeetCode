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
        minn = min(m,n)
        cor = 0 
        for i in range(minn):
            if target == matrix[i][i]:
                return True
            elif target > matrix[i][i]:
                cor = i
            else:
                break
        for r in range(0,n):
            for c in range(cor+1,m):
                if matrix[r][c] == target:
                    return True
        for c in range(0,m):
            for r in range(cor+1,n):
                if matrix[r][c] == target:
                    return True