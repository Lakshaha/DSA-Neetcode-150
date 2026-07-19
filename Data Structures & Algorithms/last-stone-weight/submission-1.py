import heapq
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        array = []
        heapq.heapify(array)
        for stone in stones:
            heapq.heappush(array, -1*stone)
        
        while len(array) > 1:
            val1 = -1* heapq.heappop(array)
            val2 = -1* heapq.heappop(array) 
            if val1 != val2:
                heapq.heappush(array, -1 * (abs(val1-val2)))
            
        if len(array) == 0:
            return 0
        return -1*array[0]
                