class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        n = len(word1)
        m = len(word2)
        i = 0
        j = 0
        result = ""

        while i < n and j < m:
            result += word1[i]
            result += word2[j]
            i+=1
            j+=1
        
        result += word1[i:]
        result += word2[j:]
        return result