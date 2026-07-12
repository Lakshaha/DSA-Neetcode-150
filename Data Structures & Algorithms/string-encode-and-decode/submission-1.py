class Solution:

    def encode(self, strs: List[str]) -> str:
        result = ""
        for word in strs:
            result += (str(len(word))+ "#" + word)
        return result        
    def decode(self, s: str) -> List[str]:
        result = []
        
        left = 0 
        
        while left < len(s):
            right = left
            while s[right] != "#":
                right += 1
            
            lent = int(s[left:right])
            left = right+1
            word = s[left:left+lent]
            left += lent
            result.append(word)
        return result