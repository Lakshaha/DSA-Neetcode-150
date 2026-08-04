class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        minHeap = []
        heapq.heapify(minHeap)
        n = len(profits)
        for i in range(n):
            p = profits[i]
            c = capital[i]
            heapq.heappush(minHeap, [c, p])

        maxHeap = []
        heapq.heapify(maxHeap)
        maxProfit = w

        for _ in range(k):
            while minHeap and minHeap[0][0] <= maxProfit:
                c,p = heapq.heappop(minHeap)
                heapq.heappush(maxHeap,-p)
            
            if not maxHeap:
                break
            
            maxProfit += -1*heapq.heappop(maxHeap)
        
        return maxProfit
        