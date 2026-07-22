class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        #check cycle detection, n-1 edgres
        if len(edges) != n-1:
            return False
        visit = set()

        hmap = defaultdict(list)
        for u,v in edges:
            hmap[u].append(v)
            hmap[v].append(u)
        queue = deque()
        queue.append(0)
        while queue:
            node = queue.popleft()
            if node in visit:
                return False
            visit.add(node)
            
            
            for i in hmap[node]:
                if i not in visit:
                    queue.append(i)
        
        return len(visit) == n
            
