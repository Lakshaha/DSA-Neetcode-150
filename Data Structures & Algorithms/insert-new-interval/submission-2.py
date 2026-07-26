class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        if not intervals:
            return [newInterval]
        intervals.append(newInterval)
        intervals.sort(key=lambda x:x[0])

        results = [intervals[0]]
        for start,end in intervals[1:]:
            lastEnd = results[-1][1]
            if start <= lastEnd:
                results[-1][1] = max(lastEnd, end)
            else:
                results.append([start,end])
        
        return results