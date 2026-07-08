class Solution:
    def longestConsecutive(self, nums):

        # Store every number inside a HashSet
        # so that lookup becomes O(1).
        numSet = set(nums)

        # Stores the longest sequence found.
        longest = 0

        # Check every number.
        for num in numSet:

            # Only start counting if
            # this number is the START
            # of a sequence.
            #
            # Example:
            #
            # 1 -> Start
            #
            # 2 -> Skip because 1 exists
            #
            # 3 -> Skip because 2 exists
            if num - 1 not in numSet:

                # Current number of sequence.
                current = num

                # Current sequence length.
                length = 1

                # Keep moving forward while
                # next consecutive number exists.
                while current + 1 in numSet:

                    current += 1
                    length += 1

                # Update answer.
                longest = max(longest, length)

        return longest
        