class Solution:
    def removeDuplicates(self, nums):

        # If array has 2 or fewer elements,
        # nothing needs to be removed.
        if len(nums) <= 2:
            return len(nums)

        # Write pointer.
        # First two elements are always allowed.
        k = 2

        # Read pointer starts from index 2.
        for i in range(2, len(nums)):

            # Compare current element with
            # the element TWO positions behind
            # in the valid answer.
            #
            # If they are different,
            # we haven't stored this number twice yet.
            if nums[i] != nums[k - 2]:

                # Keep the current element.
                nums[k] = nums[i]

                # Increase answer size.
                k += 1

        # k is the new length.
        return k