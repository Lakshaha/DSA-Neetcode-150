class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        hmap = Counter(s)
        for char in t:
            if char not in hmap or hmap[char] <= 0:
                return False
            
            hmap[char] -= 1
        
        return True