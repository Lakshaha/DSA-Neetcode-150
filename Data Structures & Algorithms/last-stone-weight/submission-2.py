class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        array = [-i for i in stones]
        heapq.heapify(array)
        while len(array) > 1:
            val1 = -1*heapq.heappop(array)
            val2 = -1*heapq.heappop(array)
            if val1 != val2:
                heapq.heappush(array, -(abs(val1-val2)))
            
        return -array[0] if array else 0