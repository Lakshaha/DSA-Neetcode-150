class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = Counter(nums)
        freq = [[] for _ in range(len(nums)+1)] #max freq can be nums only
        
        for n,c in count.items():
            freq[c].append(n)
        
        result = []
        for i in range(len(freq)-1,-1,-1):
            for j in freq[i]:
                result.append(j)
                if len(result) == k:
                    return result
                