class Solution:
    def threeSum(self, nums):

        # Step 1: Sort the array
        nums.sort()

        # Final answer
        result = []

        # Step 2: Fix one number at a time
        for i in range(len(nums)):

            # Skip duplicate fixed numbers
            # Example: [-1,-1,0,1]
            # We already processed the first -1
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            # Two pointers for remaining part
            left = i + 1
            right = len(nums) - 1

            while left < right:

                # Current triplet sum
                total = nums[i] + nums[left] + nums[right]

                # Sum too small
                # Need a bigger number
                if total < 0:
                    left += 1

                # Sum too large
                # Need a smaller number
                elif total > 0:
                    right -= 1

                # Found a valid triplet
                else:

                    result.append(
                        [nums[i], nums[left], nums[right]]
                    )

                    # Move both pointers
                    left += 1
                    right -= 1

                    # Skip duplicate left values
                    # Otherwise we'll get the same triplet again
                    while (
                        left < right and
                        nums[left] == nums[left - 1]
                    ):
                        left += 1

        return result              
