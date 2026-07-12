class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        hmap = {}
        for val in nums:
            hmap[val] = hmap.get(val,0) + 1
            if hmap[val] > 1:
                return True
        return False