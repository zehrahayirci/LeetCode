class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        res =[]
        start = intervals[0][0]        
        end = intervals[0][1]
        
        for i in range(1,len(intervals)):
            ara = intervals[i]
            if ara[0] <= end:
                #Case 2
                if ara[1] >= end:
                    end = ara[1]
            else:
                #Case 3
                res.append([start,end])
                start = ara[0]
                end = ara[1]
        res.append([start,end])
        return res
        
                