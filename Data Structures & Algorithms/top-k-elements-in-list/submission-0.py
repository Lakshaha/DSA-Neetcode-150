class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = Counter(nums)
        freqCount = defaultdict(list)
        for c in count:
            freqCount[count[c]].append(c)

        counts = list(freqCount.keys())
        counts.sort(reverse = True)
        
        result = []
        for num in counts:
            for val in freqCount[num]:
                result.append(val)
                if len(result) == k:
                    return result




