class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        #highest sum is as small as possible
        def checkMiddle(maxSum):
            numArrays = 1
            currSum = 0

            for num in nums:
                currSum += num
                if currSum > maxSum:
                    numArrays += 1
                    currSum = num
                
                if numArrays > k:
                    return False
            
            return True
        
        low = max(nums)
        high = sum(nums)
        result = high
        while low <= high:
            mid = (low + high)//2
            if checkMiddle(mid):
                result = mid
                high = mid - 1
            else:
                low = mid + 1
        
        return result