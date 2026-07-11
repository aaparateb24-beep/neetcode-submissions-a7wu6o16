class Solution:
    def rob(self, nums: List[int]) -> int:
        # If there is only one house,
        # rob it because there is no neighbour.
        if len(nums) == 1:
            return nums[0]
        # dp[i] means:
        # Maximum money we can rob
        # from houses 0 to i.
        dp = [0] * len(nums)    
        # -------------------------
        # Base Case 1
        #
        # If there is only the first house,
        # the best we can do is rob it.
        # -------------------------
        dp[0] = nums[0]
         # -------------------------
        # Base Case 2
        #
        # For the first two houses,
        # we cannot rob both.
        #
        # So choose the richer one.
        # -------------------------
        dp[1] = max(nums[0], nums[1])
        # Process remaining houses.
        for i in range(2, len(nums)):

            # -------------------------
            # Option 1:
            # Rob current house.
            #
            # Then we MUST skip
            # the previous house.
            #
            # Money =
            # Current House
            # +
            # Best till i-2
            # -------------------------
            rob_current = nums[i] + dp[i - 2]
            # -------------------------
            # Option 2:
            # Skip current house.
            #
            # Keep whatever maximum
            # money we already had
            # till previous house.
            # -------------------------
            skip_current = dp[i - 1]

            # Choose the better option.
            dp[i] = max(rob_current, skip_current)

        # Last position stores
        # the maximum money.
        return dp[-1]
        