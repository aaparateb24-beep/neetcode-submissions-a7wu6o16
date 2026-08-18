class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:

        # Stores all possible permutations.
        result = []

        # Stores the permutation we are currently building.
        subset = []

        # used[i] tells us whether nums[i] is already
        # present in the current permutation.
        #
        # Example:
        #
        # nums = [1,2,3]
        # used = [True, False, True]
        #
        # means:
        # 1 → already used
        # 2 → available
        # 3 → already used
        used = [False] * len(nums)

        def backtrack():

            # ------------------------------------------------
            # BASE CASE
            #
            # A permutation is complete when it contains
            # every number.
            # ------------------------------------------------
            if len(subset) == len(nums):

                # Add a COPY because subset will keep changing.
                result.append(subset.copy())
                return

            # ------------------------------------------------
            # Try EVERY number as the next element.
            # ------------------------------------------------
            for i in range(len(nums)):

                # ------------------------------------------------
                # If this number is already inside our current
                # permutation, we cannot use it again.
                #
                # Example:
                #
                # subset = [1,2]
                #
                # We cannot choose 1 or 2 again.
                # ------------------------------------------------
                if used[i]:
                    continue

                # ------------------------------------------------
                # CHOOSE
                #
                # Mark this number as used.
                # ------------------------------------------------
                used[i] = True

                # Add it to our current permutation.
                subset.append(nums[i])

                # ------------------------------------------------
                # RECURSE
                #
                # Now decide which unused number should
                # come next.
                # ------------------------------------------------
                backtrack()

                # ------------------------------------------------
                # BACKTRACK / UNDO
                #
                # Remove the number so that we can try
                # another number in this position.
                # ------------------------------------------------
                subset.pop()

                # Mark it as unused again.
                #
                # This is VERY important.
                #
                # Otherwise, other permutations would not
                # be able to use this number.
                used[i] = False

        # Start building the permutation.
        backtrack()

        return result