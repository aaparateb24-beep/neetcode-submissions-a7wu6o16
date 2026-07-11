class Solution:
    def climbStairs(self, n: int) -> int:
        # If there are only 1 or 2 stairs,
        # the answer is simply n.
        if n <= 2:
            return n 
        # dp[i] = number of ways
        # to reach stair i.
        dp = [0] * (n + 1)
        # Base cases
        dp[1] = 1
        dp[2] = 2

        # Build answers from
        # smaller stairs to larger stairs.
        for i in range(3, n + 1):
            dp[i] = dp[i -1] + dp[i - 2]
        return dp[n]