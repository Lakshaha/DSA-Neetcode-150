class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        lastSeen = {num:idx for idx,num in enumerate(nums)}

        for i,num in enumerate(nums):
            if i != lastSeen[num]:
                if abs(i-lastSeen[num]) <= k:
                    return True
            
        return False

        
        