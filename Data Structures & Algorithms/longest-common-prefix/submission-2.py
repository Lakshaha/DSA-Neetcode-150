class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""
        
        base = strs[0]

        for i in range(len(base)):
            for string in strs[1:]:
                if i >= len(string) or string[i] != base[i]:
                    return base[:i]
        
        return base