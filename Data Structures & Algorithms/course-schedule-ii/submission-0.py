class Solution:
    def findOrder(self, n: int, prereq: List[List[int]]) -> List[int]:
        result = []
        hmap = defaultdict(list)
        indegree = [0] * n
        queue = deque()
        for c,p in prereq:
            hmap[p].append(c)
            indegree[c] += 1
        
        for i, val in enumerate(indegree):
            if val == 0:
                queue.append(i)
            
        order = []
        while queue:
            node = queue.popleft()
            order.append(node)
            for i in hmap[node]:
                indegree[i] -= 1
                if indegree[i] == 0:
                    queue.append(i)
            
        if len(order) == n:
            return list(order)
        else:
            return []
        

        

        

