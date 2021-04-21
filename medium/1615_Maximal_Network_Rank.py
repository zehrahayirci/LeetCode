class Solution(object):
    def maximalNetworkRank(self, n, roads):
        """
        :type n: int
        :type roads: List[List[int]]
        :rtype: int
        """
        count = []
        for i in range(n):
            count.append(0)
        
        for item in roads:
            count[item[0]]+=1
            count[item[1]]+=1
        max_rank = 0
        for i in range(n):
            for j in range(i+1,n):
                rank = count[i] + count[j]
                if [i,j] in roads or [j,i] in roads:
                    rank = rank - 1
                if rank > max_rank:
                    max_rank = rank
                    sol = (i,j)
        #print(sol)
        #print(max_rank)
        return max_rank
