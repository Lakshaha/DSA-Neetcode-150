class Solution:
    def simplifyPath(self, path: str) -> str:
        path = path.split('/')
        stack = []
        for char in path:
            if char == "" or char == ".":
                continue
            elif char == "..":
                if stack:
                    stack.pop()
            else:
                stack.append(char)
        
        return "/" + "/".join(stack)

