class Solution:
    def maxAscendingSum(self, nums: List[int]) -> int:

        # Sum of the current ascending subarray
        current = nums[0]

        # Best (maximum) sum found so far
        answer = nums[0]

        # Start from the second element
        for i in range(1, len(nums)):

            # If current element is greater than
            # the previous element, the ascending
            # subarray continues.
            if nums[i] > nums[i - 1]:
                current += nums[i]

            # Otherwise, ascending order is broken.
            # Start a new subarray from nums[i].
            else:
                current = nums[i]

            # Keep track of the largest sum.
            answer = max(answer, current)

        return answer