class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        result = defaultdict(list)
        for num in arr:
            result[abs(num-x)].append(num)

        keys = list(result.keys())
        keys.sort()
        submitResult = []
        for i in keys:
            for j in result[i]:
                if len(submitResult) == k:
                    break
                submitResult.append(j)
        submitResult.sort()
        return submitResult
