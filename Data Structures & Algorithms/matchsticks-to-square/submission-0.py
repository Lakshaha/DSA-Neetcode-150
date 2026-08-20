class Solution:
    def makesquare(self, matchsticks: List[int]) -> bool:
        totalSum = sum(matchsticks)
        if totalSum % 4 != 0:
            return False
        targetSide = totalSum//4

        matchsticks.sort(reverse=True)
        if matchsticks[0] > targetSide:
            return False
        
        sides = [0] * 4
        
        def backTrack(i):
            if i == len(matchsticks):
                return True
            
            for j in range(4):
                if sides[j] + matchsticks[i] <= targetSide:
                    sides[j] += matchsticks[i]
                    if backTrack(i+1):
                        return True
                    
                    sides[j] -= matchsticks[i]
                
                if sides[j] == 0:
                    break
            return False
            
        return backTrack(0)
