class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        count = Counter(nums)
        n = len(nums)
        n //= 3
        result = []

        for i in count:
            if count[i] > n:
                result.append(i)

        return result   