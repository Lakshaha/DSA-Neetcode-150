class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.split()
        s = "".join(s)
        s = s.lower()
        left = 0
        right = len(s) - 1
        result = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'
        while left < right:
            if s[left] not in result:
                left += 1
                continue
            if s[right] not in result:
                right -= 1
                continue
            if s[left] != s[right]:
                return False
            left += 1
            right -= 1
        
        return True