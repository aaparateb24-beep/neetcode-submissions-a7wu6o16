class Solution:
    def maxProduct(self, nums):

        # Store final answer
        res = max(nums)

        # Current maximum product
        curMax = 1

        # Current minimum product
        # (important because negative × negative = positive)
        curMin = 1

        for n in nums:

            # Save old curMax before updating
            temp = curMax * n

            # Three choices:
            # 1. Start fresh from current number
            # 2. Extend previous maximum product
            # 3. Extend previous minimum product
            curMax = max(
                n,
                temp,
                curMin * n
            )

            # Similarly update minimum product
            curMin = min(
                n,
                temp,
                curMin * n
            )

            # Update global answer
            res = max(res, curMax)

        return res  


            
        