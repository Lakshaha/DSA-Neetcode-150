class Solution:
    def integerBreak(self, n: int) -> int:
        
        if n <= 3:
            if n == 2:
                return 1
            if n == 3:
                return 2
        
        numThree = n//3
        rem = n%3

        if rem == 0:
            return 3**(numThree)
        if rem == 1:
            return 3**(numThree-1) * (4)
        if rem == 2:
            return 3**(numThree) * 2