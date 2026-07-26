class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        hmap = Counter(s)
        lastSeen = {char:i for i, char in enumerate(s)}
        boundary = 0
        start = 0
        n = len(s)
        result = []
        for i,char in enumerate(s):
            boundary = max(boundary, lastSeen[char])

            if boundary == i:
                result.append(i-start+1)
                start = i + 1
        
        return result


