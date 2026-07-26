class Solution:
    def isHappy(self, n: int) -> bool:
        seen = set()
        while n != 1 and n not in seen:
            seen.add(n)
            totalDig = 0
            while n > 0:
                dig = n%10
                totalDig += (dig * dig)
                n //= 10
            n = totalDig
        
        return n == 1