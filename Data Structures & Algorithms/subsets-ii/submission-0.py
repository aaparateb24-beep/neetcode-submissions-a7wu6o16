class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:

        # ------------------------------------------------
        # Sort the array first.
        #
        # Example:
        #
        # [1,2,1]
        #
        # becomes:
        #
        # [1,1,2]
        #
        # This is IMPORTANT because duplicate values
        # will now be next to each other.
        # ------------------------------------------------
        nums.sort()

        # Stores all unique subsets.
        result = []

        # Current subset that we are building.
        subset = []

        def backtrack(start):

            # ------------------------------------------------
            # Every subset we create is a valid answer.
            #
            # So add a COPY of the current subset.
            #
            # We need .copy() because 'subset' keeps changing
            # during backtracking.
            # ------------------------------------------------
            result.append(subset.copy())

            # ------------------------------------------------
            # Try every possible next element.
            #
            # We start from 'start' so that we never go
            # backwards and create permutations.
            # ------------------------------------------------
            for i in range(start, len(nums)):

                # ------------------------------------------------
                # DUPLICATE CHECK
                #
                # Suppose:
                #
                # nums = [1,1,2]
                #
                # At the SAME recursion level:
                #
                # first 1 → allowed
                # second 1 → skip
                #
                # Otherwise we would generate the same subset
                # twice.
                #
                # IMPORTANT:
                #
                # i > start means:
                # "This is not the first choice at this level."
                #
                # So we skip only duplicate choices at the
                # SAME level.
                # ------------------------------------------------
                if i > start and nums[i] == nums[i - 1]:
                    continue

                # ------------------------------------------------
                # CHOOSE
                #
                # Add nums[i] to our current subset.
                # ------------------------------------------------
                subset.append(nums[i])

                # ------------------------------------------------
                # RECURSE
                #
                # i + 1 means the next decision can only use
                # elements AFTER the current element.
                # ------------------------------------------------
                backtrack(i + 1)

                # ------------------------------------------------
                # BACKTRACK / UNDO
                #
                # Remove the element we just chose.
                #
                # This allows us to try another possibility.
                # ------------------------------------------------
                subset.pop()

        # Start from index 0.
        backtrack(0)

        return result