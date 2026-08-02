class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        maxHeap = []
        heapq.heapify(maxHeap)
        result = []
        if a>0 : heapq.heappush(maxHeap, [-a, "a"])
        if b>0 :heapq.heappush(maxHeap, [-b, "b"])
        if c>0 :heapq.heappush(maxHeap, [-c, "c"])

        while maxHeap:
            count1, char1 = heapq.heappop(maxHeap)
            count1 = -count1

            if len(result) >= 2 and result[-1] == char1 and result[-2] == char1:
                if not maxHeap:
                    break
                count2, char2 = heapq.heappop(maxHeap)
                count2 += 1
                if count2 < 0:
                    heapq.heappush(maxHeap, [count2, char2])
                result.append(char2)
                heapq.heappush(maxHeap, [-count1, char1])
            else:
                result.append(char1)
                count1 -= 1
                if count1 > 0:
                    heapq.heappush(maxHeap, [-count1, char1])
            
        return "".join(result)
                


        