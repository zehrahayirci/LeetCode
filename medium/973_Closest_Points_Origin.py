import heapq
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        lengths =[]
        for i in points:
            length = sqrt(i[0]*i[0]+i[1]*i[1])
            lengths.append((length,i))
        heapq.heapify(lengths)
        res = []
        while k:
            res.append(heapq.heappop(lengths)[1])
            k-=1
        return res