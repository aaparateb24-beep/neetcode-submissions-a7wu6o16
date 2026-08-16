class Solution:
    def combinationSum2(self, candidates, target):

        # Sorting is VERY important.
        #
        # Example:
        # [9,2,2,4,6,1,5]
        #
        # becomes:
        # [1,2,2,4,5,6,9]
        #
        # Now duplicate values are next to each other,
        # which allows us to skip duplicate branches.
        candidates.sort()

        result = []
        path = []

        def backtrack(start, remaining):

            # =====================================================
            # BASE CASE:
            #
            # If remaining == 0, the numbers in path add up
            # exactly to target.
            # =====================================================
            if remaining == 0:
                result.append(path.copy())
                return

            # We try every candidate starting from 'start'.
            for i in range(start, len(candidates)):

                # =================================================
                # DUPLICATE SKIPPING
                #
                # Suppose we have:
                #
                # [1,2,2,4]
                #
                # At the same recursion level, choosing the first
                # 2 and choosing the second 2 would create the same
                # combinations.
                #
                # So skip the second 2.
                #
                # IMPORTANT:
                #
                # i > start means:
                # "Is this a duplicate at THIS recursion level?"
                #
                # We do NOT simply write:
                #
                # candidates[i] == candidates[i-1]
                #
                # because that could incorrectly prevent us from
                # choosing two 2s in the same combination.
                # =================================================
                if i > start and candidates[i] == candidates[i - 1]:
                    continue

                # =================================================
                # PRUNING
                #
                # Because candidates is sorted, if the current
                # number is already greater than remaining,
                # every number after it will also be too large.
                #
                # Therefore we can stop the loop completely.
                # =================================================
                if candidates[i] > remaining:
                    break

                # =================================================
                # CHOOSE
                # =================================================
                path.append(candidates[i])

                # =================================================
                # EXPLORE
                #
                # IMPORTANT:
                #
                # We use i + 1.
                #
                # Why?
                #
                # Each element can only be used ONCE.
                #
                # So after choosing candidates[i], we can only
                # consider elements to its right.
                # =================================================
                backtrack(
                    i + 1,
                    remaining - candidates[i]
                )

                # =================================================
                # UNDO
                #
                # We have finished exploring every combination
                # that begins with this choice.
                #
                # Remove it so we can try the next candidate.
                # =================================================
                path.pop()

        # Start from index 0 with the full target.
        backtrack(0, target)

        return result