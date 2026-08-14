class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:

        # ------------------------------------------------
        # result stores ALL possible subsets.
        #
        # Example for [1,2]:
        #
        # [[], [1], [2], [1,2]]
        # ------------------------------------------------
        result = []

        # ------------------------------------------------
        # subset represents the subset we are currently
        # building during recursion.
        # ------------------------------------------------
        subset = []

        # ------------------------------------------------
        # BACKTRACKING FUNCTION
        #
        # i tells us which element we are currently
        # making a decision about.
        # ------------------------------------------------
        def backtrack(i):

            # ------------------------------------------------
            # BASE CASE
            #
            # If we have processed every element,
            # the current subset is complete.
            # ------------------------------------------------
            if i == len(nums):

                # IMPORTANT:
                # Add a COPY of subset.
                #
                # We use subset.copy() because subset itself
                # will continue changing during backtracking.
                result.append(subset.copy())
                return

            # =================================================
            # CHOICE 1: TAKE nums[i]
            # =================================================

            # Add the current number to our subset.
            subset.append(nums[i])

            # Move to the next element.
            backtrack(i + 1)

            # ------------------------------------------------
            # BACKTRACK / UNDO
            #
            # Remove the element we just added.
            #
            # This allows us to try the other possibility:
            # SKIP nums[i].
            # ------------------------------------------------
            subset.pop()

            # =================================================
            # CHOICE 2: SKIP nums[i]
            # =================================================

            # We don't add nums[i].
            # Simply move to the next element.
            backtrack(i + 1)

        # Start making decisions from index 0.
        backtrack(0)

        # Return all generated subsets.
        return result