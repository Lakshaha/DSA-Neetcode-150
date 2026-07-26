class Solution:
    def getSum(self, a: int, b: int) -> int:
        mask = 0xFFFFFFFF
        while b&mask:
            sumwoutcarry = a^b
            carry = (a&b) << 1
            a = sumwoutcarry
            b = carry
        
        return (a & mask) if (a & mask) <= 0x7FFFFFFF else ~((a & mask) ^ mask)
