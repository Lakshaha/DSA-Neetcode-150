class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        left = max(weights)
        right = sum(weights)
        def bs(avgW):
            days = 1
            currW = 0

            for w in weights:
                if currW + w > avgW:
                    days += 1
                    currW = 0
                currW += w
                
            return days
        
        while left <= right:
            mid = (left + right)//2
            if bs(mid) <= days:
                right = mid-1
            else:
                left = mid+1
        
        return left 
            
