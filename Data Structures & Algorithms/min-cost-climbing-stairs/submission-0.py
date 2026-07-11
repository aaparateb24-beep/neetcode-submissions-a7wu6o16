class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)
        dp = [0] * n

        # Base cases.
        # To stand on stair 0,
        # we pay cost[0].
        dp[0] = cost[0] #because we can start from either stair 1 or stair 0

        # To stand on stair 1,
        # we pay cost[1].
        dp[1] = cost[1]
        
        for i in range(2, n):
            # Cost of current stair
            # +
            # minimum of previous two stairs.
            dp[i] = cost[i] + min(dp[i - 1], dp[i -2])  
             # The top is AFTER the last stair.
        #
        # We can reach it from either
        # last stair or second last stair.
        return min(dp[n - 1], dp[n - 2]) 
