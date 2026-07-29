class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        passenger = [0] * (1001)

        for num,start,end in trips:
            passenger[start] += num
            passenger[end] -= num
        total = 0
        for change in passenger:
            total += change
            if total > capacity:
                return False
        
        return True