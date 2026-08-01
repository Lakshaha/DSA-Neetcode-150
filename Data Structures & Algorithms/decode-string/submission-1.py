class Solution:
    def decodeString(self, s: str) -> str:
        stack = [] #store string, num times
        currNum = 0
        currStr = ""
        for char in s:
            if char.isdigit():
                currNum = currNum*10 + int(char)
            elif char == '[':
                stack.append([currStr, currNum])
                currStr = ""
                currNum = 0
            elif char == "]":
                prevStr, num = stack.pop()
                currStr = prevStr + (currStr*num)
            else:
                currStr += char
        
        return currStr