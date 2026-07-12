class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for char in tokens:
            if char not in "+-/*":
                stack.append(int(char))
            else:
                a = stack.pop()
                b = stack.pop()
                if char == "+":
                    stack.append(a+b)
                elif char == "-":
                    stack.append(b-a)
                elif char == "*":
                    stack.append(b*a)
                else:
                    if a != 0:
                        stack.append(int(b/a))
        
        return int(stack[-1])