class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hmap = {}
        for i,val in enumerate(nums):
            hmap[val] = i
        
        for i,num in enumerate(nums):
            val = target - num

            if hmap.get(val) != None and hmap[val] != i:
                if i > hmap[val]:
                    return [hmap[val], i]
                else:
                    return [i, hmap[val]]
                
        return []