class Solution:
    def reverseBits(self, n: int) -> int:
        nStr = format(n,"032b")
        nStr = nStr[::-1]
        return int(nStr,2)