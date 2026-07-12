class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        low, high = 1, max(piles)
        ans = max(piles)

        while low <= high:
            speed = low + (high-low)//2

            hours = sum(math.ceil(x/speed) for x in piles)
            if hours <= h:
                ans = speed
                high = speed - 1
            else:
                low = speed + 1
        
        return ans