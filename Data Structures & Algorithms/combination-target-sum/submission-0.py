class Solution:
    def combinationSum(self, candidates, target):

        # Stores all valid combinations we find.
        result = []

        # 'path' represents the combination we are currently building.
        # Example: [2, 2, 3]
        path = []

        def backtrack(i, remaining):

            # =========================================================
            # BASE CASE 1:
            # If remaining becomes 0, our current path adds up to
            # exactly the target.
            #
            # Example:
            # target = 7
            # path = [2, 2, 3]
            # remaining = 0
            #
            # Therefore, we found a valid combination.
            # =========================================================
            if remaining == 0:
                result.append(path.copy())
                return

            # =========================================================
            # BASE CASE 2:
            # We've gone past the last candidate.
            #
            # There are no more numbers available to try.
            # =========================================================
            if i == len(candidates):
                return

            # Current number we're deciding about.
            num = candidates[i]

            # =========================================================
            # CHOICE 1: TAKE candidates[i]
            #
            # We can only take it if it doesn't make the sum exceed
            # our target.
            #
            # Example:
            # remaining = 5
            # num = 2
            #
            # We can take 2.
            # New remaining = 5 - 2 = 3
            # =========================================================
            if num <= remaining:

                # Make the choice.
                path.append(num)

                # -----------------------------------------------------
                # IMPORTANT:
                #
                # We call backtrack(i, ...)
                # NOT backtrack(i + 1, ...)
                #
                # Why?
                #
                # Because Combination Sum allows us to use the SAME
                # number unlimited times.
                #
                # So if we chose 2:
                #
                # [2]
                # [2,2]
                # [2,2,2]
                #
                # We stay at index i so that 2 is available again.
                # -----------------------------------------------------
                backtrack(i, remaining - num)

                # -----------------------------------------------------
                # UNDO THE CHOICE
                #
                # The recursive call above explored EVERY possibility
                # that starts with the current path.
                #
                # Now we come back and remove 'num' so that we can
                # try another possibility.
                #
                # This is the BACKTRACKING step.
                # -----------------------------------------------------
                path.pop()

            # =========================================================
            # CHOICE 2: SKIP candidates[i]
            #
            # We've decided:
            #
            # "I don't want to use this number anymore."
            #
            # Therefore, move to the NEXT candidate.
            #
            # i + 1 means:
            #
            # current candidate → DONE
            # next candidate    → TRY
            # =========================================================
            backtrack(i + 1, remaining)

        # Start from:
        #
        # i = 0
        # → first candidate
        #
        # remaining = target
        # → nothing has been chosen yet
        backtrack(0, target)

        return result
        