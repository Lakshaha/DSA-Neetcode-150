class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        memo = {}
        n = len(coins)

        def dfs(i, remSum):
            if remSum == 0:
                return 1 #need not add anymore coins
            if remSum < 0 or i >= n:
                return 0
            if (i,remSum) in memo:
                return memo[(i,remSum)]
            take = dfs(i, remSum-coins[i])
            skip = dfs(i+1, remSum)
            memo[(i,remSum)] = take + skip
            return memo[(i,remSum)]
            



        
        return dfs(0,amount)
           