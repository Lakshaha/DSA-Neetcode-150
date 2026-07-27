class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not s or not t:
            return ""
        
        countT = Counter(t)
        window = {}
        have = 0
        need = len(countT)
        maxLen = float("inf")
        result = [-1,-1]
        l = 0
        for r in range(len(s)):
            c = s[r]
            window[c] = window.get(c,0) + 1

            if c in countT and countT[c] == window[c]:
                have += 1
            
            while have == need:
                if (r-l+1) < maxLen:
                    maxLen = r-l+1
                    result = [l,r]
                
                window[s[l]] -= 1
                if s[l] in countT and window[s[l]] < countT[s[l]]:
                    have -= 1
                
                l += 1
            
        l,r = result
        return s[l:r+1] if maxLen != float('inf') else ""
