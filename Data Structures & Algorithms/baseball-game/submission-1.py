class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack = []
        for i in operations:
            if i == "+":
                val1 = stack.pop() if len(stack) > 0 else 0
                val2 = stack.pop() if len(stack) > 0 else 0
                stack.append(val2)
                stack.append(val1)
                stack.append(val1+val2)
            elif i == "D":
                val1 = stack.pop() if len(stack) > 0 else 0
                stack.append(val1)
                stack.append(2*val1)
            elif i == "C":
                val1 = stack.pop() if len(stack) > 0 else 0
            else:
                stack.append(int(i))
        return sum(stack) if len(stack) > 0 else 0 