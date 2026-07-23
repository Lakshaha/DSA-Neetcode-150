class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        hmap = defaultdict(list)
        for sou,des in tickets:
            hmap[sou].append(des)
        
        for sou in hmap:
            hmap[sou].sort(reverse=True)
        
        itin = []

        def dfs(airport):
            while hmap[airport]:
                nextdes = hmap[airport].pop()
                dfs(nextdes)
            itin.append(airport)
        
        dfs("JFK")
        return itin[::-1]