class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        globalMaxProd = nums[0]
        currMaxProd = nums[0]
        currMinProd = nums[0]

        for i in nums[1:]:
            tempMax = max(i, currMaxProd*i, currMinProd*i)
            currMinProd = min(i, currMaxProd*i, currMinProd*i)
            currMaxProd = tempMax

            globalMaxProd = max(globalMaxProd, currMaxProd)
        
        return globalMaxProd