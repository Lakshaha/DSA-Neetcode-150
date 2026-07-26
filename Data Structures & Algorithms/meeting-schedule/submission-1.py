"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        if not intervals:
            return True
        intervals.sort(key=lambda x:x.start)
        endTime = intervals[0].end
        for i in (intervals[1:]):
            if i.start < endTime:
                return False
            endTime = i.end
        
        return True