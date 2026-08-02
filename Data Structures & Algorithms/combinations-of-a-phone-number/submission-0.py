class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        hmap = {
            2:"abc", 3:"def", 4: "ghi", 5: "jkl", 6: "mno", 7:"pqrs", 8:"tuv", 9:"wxyz"
        }
        result = []
        def bt(i, subArray):
            if i == len(digits):
                result.append("".join(subArray))
                return
            
            num = int(digits[i])
            for char in hmap[num]:
                subArray.append(char)
                bt(i+1, subArray)
                subArray.pop()
        
        bt(0,[])
        return result

