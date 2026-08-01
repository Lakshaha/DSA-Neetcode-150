class Solution:
    def simplifyPath(self, path: str) -> str:
        newPath = path.split('/')
        stack = []
        for char in newPath:
            if char == "" or char == ".":
                continue
            elif char == "..":
                if stack:
                    stack.pop()
            else:
                stack.append(char)
        
        return "/" + "/".join(stack)