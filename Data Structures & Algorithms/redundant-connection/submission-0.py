class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n = len(edges)
        parent = list(range(n+1))
        rank = [-1] * (n+1)

        def findParent(x):
            if x != parent[x]:
                parent[x] = findParent(parent[x])
            return parent[x]

        def union(a,b):
            pa = findParent(a)
            pb = findParent(b)
            if pa == pb:
                return False
            if rank[pa] > rank[pb]:
                parent[pb] = pa
            elif rank[pb] > rank[pa]:
                parent[pa] = pb
            else:
                parent[pa] = pb
                rank[pb] += 1
            return True
        result = []
        for a,b in edges:
            if not union(a,b):
                result.append([a,b])

        if len(result) != 0:
            return result[-1]
        return [-1,-1]