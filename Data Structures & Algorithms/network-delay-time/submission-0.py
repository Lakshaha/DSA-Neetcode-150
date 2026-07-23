class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        hmap = defaultdict(list)
        for u,v,w in times:
            hmap[u].append((w,v))
        visit = set()
        min_heap = []
        heapq.heapify(min_heap)
        heapq.heappush(min_heap, (0,k)) #curr time, which node
        while min_heap:
            time,node = heapq.heappop(min_heap)
            if node in visit:
                continue
            visit.add(node)
            if len(visit) == n:
                return time
            for t,v in hmap[node]:
                heapq.heappush(min_heap, (time+t, v))
        return -1
