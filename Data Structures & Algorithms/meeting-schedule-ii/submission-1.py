"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        start = []
        end = []
        for i in intervals:
            start.append(i.start)
            end.append(i.end)
        
        start.sort()
        end.sort()
        numRooms = 0
        maxRooms = 0
        s = 0
        e = 0
        while s < len(start):
            if start[s] < end[e]:
                s += 1
                numRooms += 1
            else:
                e += 1
                numRooms -= 1

            maxRooms = max(numRooms, maxRooms)
        
        return maxRooms
