class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        result = []
        perm = []
        count = Counter(nums)

        def dfs(i, perm):
            if len(perm) == len(nums):
                result.append(perm[:])
                return
            
            for n in count:
                if count[n] > 0:
                    perm.append(n)
                    count[n] -= 1

                    dfs(i+1,perm)

                    count[n] += 1
                    perm.pop()
        
        dfs(0,perm)
        return result