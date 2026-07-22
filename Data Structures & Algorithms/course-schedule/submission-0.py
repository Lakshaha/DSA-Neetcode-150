class Solution:
    def canFinish(self, n: int, prereq: List[List[int]]) -> bool:
        #topological sort
        indegree = [0] * (n)
        hmap = defaultdict(list)
        visit = set()

        for c,p in prereq:
            hmap[p].append(c)
            indegree[c] += 1
        queue = deque()
        for i, val in enumerate(indegree):
            if val == 0:
                queue.append(i)
            
        
        while queue:
            node = queue.popleft()
            for i in hmap[node]:
                indegree[i] -= 1
                if indegree[i] == 0:
                    queue.append(i)

        return sum(indegree) == 0
        