import heapq
from collections import deque

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        counter = Counter(tasks)
        max_heap = [-cnt for cnt in counter.values()]
        heapq.heapify(max_heap)

        time = 0
        cooldown_queue = deque()

        while max_heap or cooldown_queue:
            time += 1
            if max_heap:
                cnt = heapq.heappop(max_heap) + 1
                if cnt != 0:
                    cooldown_queue.append([cnt, time+n])

            if cooldown_queue and cooldown_queue[0][1] == time:
                cnt = cooldown_queue.popleft()[0]
                heapq.heappush(max_heap, cnt)

        return time 