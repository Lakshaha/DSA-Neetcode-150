class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        tortoise = nums[0]
        hare = nums[0]

        while True:
            tortoise = nums[tortoise]
            hare = nums[nums[hare]]
            if tortoise == hare:
                break
            
        
        tort = nums[0]
        while tort != hare:
            tort = nums[tort]
            hare = nums[hare]
            
        return tort

