class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        self.totalSum = 0
        def subset(i, subs):
            if i == len(nums):
                currXor = 0
                for i in subs:
                    currXor ^= i
                
                self.totalSum += currXor
                return
            
            subs.append(nums[i])
            subset(i+1, subs)
            subs.pop()
            subset(i+1, subs)

        
        subset(0,[])
        return self.totalSum