class Solution:
    def hammingWeight(self, n: int) -> int:
      string = bin(n)[2:]
      return string.count("1")
        