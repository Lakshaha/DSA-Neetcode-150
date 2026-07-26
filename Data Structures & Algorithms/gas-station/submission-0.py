class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if sum(gas) < sum(cost):
            return -1
        
        startIdx = 0
        totalTank = 0

        for i in range(len(gas)):
            totalTank += (gas[i] - cost[i])
            if totalTank < 0:
                startIdx=i+1
                totalTank = 0
        
        return startIdx