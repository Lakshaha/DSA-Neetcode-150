class Solution:
    def rob(self, nums: List[int]) -> int:
        m = len(nums)

        def check(array):
            n = len(array)
            if n < 2:
                return max(array)
            dp = [0] * (n+1)
            dp[0] = array[0]
            dp[1] = max(array[0], array[1])
            for i in range(2,n):
                dp[i] = max(dp[i-1], array[i] + dp[i-2])
            
            return dp[n-1]
        if m > 1:
            return max(check(nums[:m-1]), check(nums[1:]))
        else:
            if m == 1:
                return nums[0]
            else:
                return 0

        