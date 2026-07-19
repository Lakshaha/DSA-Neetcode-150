class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        array = []
        heapq.heapify(array)

        for x,y in points:
            heapq.heappush(array, (-1*(x**2 + y**2), x,y))
            if len(array) > k:
                heapq.heappop(array)
            
        
        return [[x,y] for dist,x,y in array]