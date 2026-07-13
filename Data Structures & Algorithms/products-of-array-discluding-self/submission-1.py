class Solution:
    def productExceptSelf(self, nums):

        # Length of the array
        n = len(nums)

        # Final answer array.
        #
        # Initially every value is 1 because
        # multiplication identity is 1.
        answer = [1] * n

        # ------------------------------------------------
        # LEFT PASS
        #
        # After this loop,
        #
        # answer[i]
        #
        # stores the product of
        # every element to the LEFT of i.
        #
        # Example:
        #
        # nums = [2,5,4,10]
        #
        # answer becomes
        #
        # [1,2,10,40]
        # ------------------------------------------------
        for i in range(1, n):

            # Left Product
            #
            # Previous Left Product
            #
            # ×
            #
            # Previous Number
            answer[i] = answer[i - 1] * nums[i - 1]

        # ------------------------------------------------
        # RIGHT PASS
        #
        # Instead of creating another array,
        # we keep only ONE variable called "right".
        #
        # right stores the product of
        # everything to the RIGHT of current index.
        # ------------------------------------------------
        right = 1

        # Traverse from right to left.
        for i in range(n - 1, -1, -1):

            # Final Answer
            #
            # =
            #
            # Left Product
            #
            # ×
            #
            # Right Product
            answer[i] *= right

            # Update the right product
            # for the next iteration.
            #
            # Example
            #
            # right = 1
            #
            # then
            #
            # right = 1 * nums[last]
            #
            # then
            #
            # right = previous_right * nums[i]
            right *= nums[i]

        # Return the final product array.
        return answer