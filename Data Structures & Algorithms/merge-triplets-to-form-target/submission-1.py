class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        maxA, maxB, maxC = float("-inf"), float("-inf"), float("-inf")
        for a,b,c in triplets:
            if a > target[0] or b > target[1] or c > target[2]:
                continue

            maxA = max(maxA, a)
            maxB = max(maxB, b)
            maxC = max(maxC, c)
    
        return maxA == target[0] and maxB == target[1] and maxC == target[2]
    