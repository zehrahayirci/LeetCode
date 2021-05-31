class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        m = len(grid) #row
        n = len(grid[0]) #column
        if m == n ==1:
            return grid[0][0]
        dp = m * [n*[0]]
        #print(dp)
        dp[0][0] = grid[0][0]
        for i in range(m):
            for j in range(n):
                if i==0 and j != 0:
                    dp[i][j] = grid[i][j] + dp[i][j-1]
                elif i != 0 and j ==0:
                    dp[i][j] = grid[i][j] + dp[i-1][j]
                else:
                    dp[i][j] = min(dp[i][j-1],dp[i-1][j])+grid[i][j]
        #print(dp)
        return dp[i][j]
            