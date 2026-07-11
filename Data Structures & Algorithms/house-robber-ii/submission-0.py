class Solution:
    def rob(self, nums):

        # Only one house.
        if len(nums) == 1:
            return nums[0]

        # Same House Robber I function.
        def helper(arr):

            if len(arr) == 1:
                return arr[0]

            prev2 = arr[0]
            prev1 = max(arr[0], arr[1])

            for i in range(2, len(arr)):
                current = max(arr[i] + prev2, prev1)

                prev2 = prev1
                prev1 = current

            return prev1

        # Case 1:
        # Ignore last house.
        rob_first = helper(nums[:-1])

        # Case 2:
        # Ignore first house.
        rob_last = helper(nums[1:])

        # Best of both cases.
        return max(rob_first, rob_last)
        