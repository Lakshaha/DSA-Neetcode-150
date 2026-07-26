class Solution:
    def jump(self, nums: List[int]) -> int:
        n = len(nums)
        if n <= 1:
            return 0

        jump = 0
        currEnd = 0
        farthest = 0

        for i in range(n-1):
            farthest = max(farthest, i + nums[i])

            if i == currEnd:
                jump += 1
                currEnd = farthest

            if currEnd >= n-1:
                break

        return jump 