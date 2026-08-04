class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:        
        low = 1
        high = max(piles)
        minHours = high
        totalBananas = sum(piles)

        while low <= high:
            mid = (low + high)//2
            currHours = sum(math.ceil(x/mid) for x in piles)
            if currHours <= h:
                minHours = currHours
                high = mid-1
            else:
                low = mid +1
            
        
        return low



        