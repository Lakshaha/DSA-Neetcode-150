class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        if not intervals:
            return 0
        
        intervals.sort(key=lambda x:x[1])
        #sorted on start time
        count = 0
        endTime = intervals[0][1]
        for start, end in intervals[1:]:
            if start < endTime:
                count +=1
            else:
                endTime = end
        
        return count