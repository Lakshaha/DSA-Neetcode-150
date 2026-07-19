class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        result = []
        def bt(subset, start_idx, currSum):
            if currSum == target:
                result.append(subset[:])
                return
            
            for i in range(start_idx, len(candidates)):
                if i > start_idx and candidates[i] == candidates[i-1]:
                    continue
                
                if currSum + candidates[i] > target:
                    break
                
                subset.append(candidates[i])

                bt(subset, i+1, currSum + candidates[i])

                subset.pop()
        
        bt([], 0, 0)
        return result