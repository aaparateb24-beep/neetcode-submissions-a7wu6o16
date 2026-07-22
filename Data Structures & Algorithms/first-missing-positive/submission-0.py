class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        n = len(nums)
        i = 0
        # Correct position for current number.
            #
            # Example:
            #
            # Number 5
            #
            # should be at index 4
        while i < n:
            correct = nums[i] - 1
        # Swap only if:
            #
            # 1. Number is positive.
            # 2. Number is within array size.
            # 3. Number is not already in its correct position 
            if (1 <= nums[i] <= n 
            and nums[i] != nums[correct]):
                nums[i], nums[correct] = nums[correct], nums[i]
            else:
                i += 1
        
        #
        # Find the first position where
        # expected number is missing.
        for i in range(n):
            if nums[i] != i + 1:
                return i + 1
        # All numbers 1...n exist.
        #
        # So answer is n+1.
        # ----------------------------------------
        return n + 1            

        