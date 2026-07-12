class Solution:
    def isValid(self, s: str) -> bool:
        hmap = {')':'(', '}':'{', ']':'['}
        stack = []
        for char in s:
            if char in hmap:
                topChar = stack.pop() if stack else "#"
                if topChar != hmap[char]:
                    return False
            else:
                stack.append(char)
        
        return not stack