class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:

        # ------------------------------------------------
        # SORT THE ARRAY
        #
        # Example:
        #
        # [2,1,1]
        #
        # becomes:
        #
        # [1,1,2]
        #
        # Now duplicate values are next to each other,
        # so we can easily detect them.
        # ------------------------------------------------
        nums.sort()

        # Stores all unique permutations.
        result = []

        # Current permutation that we are building.
        subset = []

        # used[i] tells us whether nums[i] is already
        # being used in the current permutation.
        used = [False] * len(nums)

        def backtrack():

            # ------------------------------------------------
            # BASE CASE
            #
            # If our permutation contains every element,
            # we have completed one permutation.
            # ------------------------------------------------
            if len(subset) == len(nums):

                # Add a COPY because subset will change
                # during backtracking.
                result.append(subset.copy())
                return

            # ------------------------------------------------
            # Try every number as the next element.
            # ------------------------------------------------
            for i in range(len(nums)):

                # ------------------------------------------------
                # If this particular element is already being
                # used in our current permutation, we cannot
                # use it again.
                # ------------------------------------------------
                if used[i]:
                    continue

                # ------------------------------------------------
                # DUPLICATE CHECK
                #
                # nums is sorted, so:
                #
                # nums[i] == nums[i-1]
                #
                # means these are duplicate values.
                #
                # We skip the current duplicate ONLY when the
                # previous identical element is NOT being used.
                #
                # That means the previous copy is available at
                # the SAME recursion level.
                #
                # Example:
                #
                # [1,1,2]
                #
                # At the first level:
                #
                # choose first 1 → explore
                # choose second 1 → SKIP
                #
                # But after choosing first 1:
                #
                # [1]
                #
                # we ARE allowed to choose the second 1 because
                # the first 1 is currently used.
                # ------------------------------------------------
                if i > 0 and nums[i] == nums[i - 1] and not used[i - 1]:
                    continue

                # ------------------------------------------------
                # CHOOSE
                # ------------------------------------------------
                used[i] = True
                subset.append(nums[i])

                # Explore all possibilities after choosing
                # this number.
                backtrack()

                # ------------------------------------------------
                # BACKTRACK / UNDO
                #
                # Remove the number so we can try another
                # possibility at this position.
                # ------------------------------------------------
                subset.pop()
                used[i] = False

        # Start building permutations.
        backtrack()

        return result