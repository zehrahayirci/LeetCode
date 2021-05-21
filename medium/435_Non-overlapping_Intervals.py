class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        if len(intervals) ==0:
            return 0
        intervals.sort()
        end = intervals[0][1]
        prev = 0
        count = 0
        for i in range(1,len(intervals)):
            event = intervals[i]
            print(intervals[prev],event,count)
            if intervals[prev][1] > event[0]:
                if intervals[prev][1] > event[1]:
                    prev = i
                #this must be exlcluded
                count+=1
            else:
                prev =i
        return count