class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if not nums:
            return 0
        writeIdx = 1

        for i in range(1,len(nums)):
            if nums[i] != nums[writeIdx-1]:
                nums[writeIdx] = nums[i]
                writeIdx += 1
            
        return writeIdx
