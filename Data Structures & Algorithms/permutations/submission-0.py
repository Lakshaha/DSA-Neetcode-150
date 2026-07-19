class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        result = []
        visited = set()
        def bt(subset):
            if len(subset) == len(nums):
                result.append(subset[:])
                return
            
            for num in nums:
                if num in visited:
                    continue 
                
                subset.append(num)
                visited.add(num)

                bt(subset)

                subset.pop()
                visited.remove(num)
            

        bt([])
        return result
