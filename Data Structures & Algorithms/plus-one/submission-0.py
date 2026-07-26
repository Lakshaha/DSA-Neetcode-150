class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        n = len(digits)
        results = [0]*(n+1)
        carry = 0
        for i in range(n-1,-1,-1):
            if i == (n-1):
                val = digits[i] + 1
            else:
                val = digits[i] + carry
            
            carry = val//10
            results[i+1] = val % 10
        if carry == 0:
            return results[1:]
        else:
            results[0] = carry
            return results

