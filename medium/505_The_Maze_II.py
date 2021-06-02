class Solution:
    def shortestDistance(self, maze: List[List[int]], start: List[int], destination: List[int]) -> int:
    
        R, C = len(maze), len(maze[0])
        dp = [[float('inf')] * C for _ in range(R)]
        dp[start[0]][start[1]] = 0
        heap = [(0, start)]
        visited = set()
        while heap:
            _, (i, j) = heapq.heappop(heap)
            visited.add((i, j))
            for dx, dy in ((0,-1),(0,1),(-1,0),(1,0)):
                x, y, d = i, j, 0
                while 0 <= x+dx < R and 0 <= y+dy < C and not maze[x+dx][y+dy]:
                    x, y, d = x+dx, y+dy, d+1
                if (x, y) not in visited and (nd := dp[i][j] + d) < dp[x][y]:
                    dp[x][y] = nd
                    heapq.heappush(heap, (nd, (x, y)))
        i, j = destination
        return dp[i][j] if dp[i][j] != float('inf') else -1