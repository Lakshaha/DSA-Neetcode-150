class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        count = 0
        hmap = defaultdict(list)
        for u,v in edges:
            hmap[u].append(v)
            hmap[v].append(u)
        visit = set()

        def bfs(node):
            if node in visit:
                return
            
            visit.add(node)
            for i in hmap[node]:
                if i not in visit:
                    bfs(i)

        for i in range(n):
            if i not in visit:
                bfs(i)
                count += 1
        
        return count