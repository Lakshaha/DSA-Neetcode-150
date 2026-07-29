class Solution:
    def reorganizeString(self, s: str) -> str:
        count = Counter(s)

        maxHeap = [(-count, char) for char,count in count.items()]
        heapq.heapify(maxHeap)
        prevCount, prevChar = 0, ""
        res = []

        while maxHeap:
            count, char = heapq.heappop(maxHeap)
            res.append(char)
            if prevCount < 0:
                heapq.heappush(maxHeap, (prevCount, prevChar))
            
            prevCount, prevChar = count+1, char
        
        res = "".join(res)
        return res if len(res) == len(s) else ""
