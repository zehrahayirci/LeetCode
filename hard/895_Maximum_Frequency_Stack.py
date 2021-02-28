class FreqStack(object):

    def __init__(self):
        self.frequency = collections.Counter()
        self.counts = collections.defaultdict(list)
        self.mostFrequent = 0 
            

    def push(self, x):
        """
        :type x: int
        :rtype: None
        """

        self.frequency[x] +=1
        self.mostFrequent = max(self.mostFrequent,self.frequency[x])
        self.counts[self.frequency[x]].append(x)
            

    def pop(self):
        """
        :rtype: int
        """
        x = self.counts[self.mostFrequent].pop()
        if not self.counts[self.mostFrequent]: 
            self.mostFrequent = self.mostFrequent - 1                              
        self.frequency[x] -=1
        return x 
        

        
        


# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(x)
# param_2 = obj.pop()