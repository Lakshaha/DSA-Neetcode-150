class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        open_n = 0
        close_n = 0
        result = []
        def bt(open_n, close_n, stack):
            if open_n == close_n == n:
                result.append(stack[:])
                return
            if open_n < n:
                bt(open_n+1, close_n, stack + "(")
            if close_n < open_n:
                bt(open_n, close_n+1, stack + ")")
        
        bt(0,0,"")
        return result
