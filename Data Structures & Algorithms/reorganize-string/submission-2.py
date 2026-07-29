class Solution:
    def reorganizeString(self, s: str) -> str:
        count = Counter(s)
        
        maxHeap = []
        heapq.heapify(maxHeap)
        for char,count in count.items():
            heapq.heappush(maxHeap, (-count,char))

        result = []
        i = 0
        n = len(s)
        prevCount, prevChar = 0, ""

        while maxHeap:
            count, char = heapq.heappop(maxHeap)
            result.append(char)
            
            if prevCount < 0:
                heapq.heappush(maxHeap, (prevCount, prevChar))
            
            prevCount, prevChar = count+1, char
        
        result = "".join(result)
        return result if len(result) == len(s) else ""