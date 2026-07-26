class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        if "0" in [num1,num2]:
            return "0"
        n = len(num1)
        m = len(num2)
        result = [0] * (n+m)
        num1 = num1[::-1]
        num2 = num2[::-1]

        for i in range(n):
            for j in range(m):
                dig = int(num1[i]) * int(num2[j])
                result[i+j] += dig
                result[i+j+1] += result[i+j]//10
                result[i+j] = result[i+j]%10
        
        start_idx = 0
        result = result[::-1]
        while start_idx < len(result) and result[start_idx] == 0:
            start_idx += 1
        
        return "".join(map(str,result[start_idx:]))
