class MedianFinder:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.minheap = []
        self.maxheap = []

    def addNum(self, num: int) -> None:
        heapq.heappush (self.maxheap ,-heapq.heappushpop(self.minheap , num) )
        if len(self.maxheap) > len(self.minheap):
            heapq.heappush( self.minheap, -heapq.heappop(self.maxheap))

            

    def findMedian(self) -> float:
        if len(self.maxheap) == len(self.minheap):
            return (self.minheap[0] + -self.maxheap[0]) / 2.
        return self.minheap[0]


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()