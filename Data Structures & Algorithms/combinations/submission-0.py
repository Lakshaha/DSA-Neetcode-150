class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        result = []
        def bt(start, currArray):
            if len(currArray) == k:
                result.append(currArray[:])
                return
            
            need = k - len(currArray)
            for i in range(start, n-need+2):
                currArray.append(i)
                bt(i+1, currArray)
                currArray.pop()
        
        bt(1,[])
        return result