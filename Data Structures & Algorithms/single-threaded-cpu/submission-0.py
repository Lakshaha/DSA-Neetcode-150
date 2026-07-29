class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        
        extendedTasks = []
        for idx, (enq, proc) in enumerate(tasks):
            extendedTasks.append([enq, proc, idx])
        
        extendedTasks.sort(key= lambda x:x[0])

        minHeap = []
        heapq.heapify(minHeap)
        res = []
        currTime = 0
        i = 0
        n = len(tasks)

        while i < n or minHeap:
            if not minHeap and currTime < extendedTasks[i][0]:
                currTime = extendedTasks[i][0]
            
            while i < n and  extendedTasks[i][0] <= currTime:
                heapq.heappush(minHeap, [extendedTasks[i][1], extendedTasks[i][2]])
                i += 1
            
            proc, idx = heapq.heappop(minHeap)
            currTime += proc
            res.append(idx)
        
        return res