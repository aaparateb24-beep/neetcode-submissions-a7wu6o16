class Solution:
    def combine(self, n: int, k: int):

        # Stores all valid combinations.
        result = []

        # Stores the combination we're currently building.
        path = []

        def backtrack(start, k):

            # =====================================================
            # BASE CASE
            #
            # We have selected exactly k numbers.
            #
            # Example:
            # k = 0
            # path = [1, 2]
            #
            # This is a complete combination.
            # =====================================================
            if k == 0:
                result.append(path.copy())
                return

            # =====================================================
            # Try every number from 'start' through 'n'.
            #
            # 'start' prevents us from going backwards.
            #
            # If we chose 2, we only consider 3, 4, ...
            # =====================================================
            for i in range(start, n + 1):

                # =================================================
                # CHOOSE
                # =================================================
                path.append(i)

                # =================================================
                # EXPLORE
                #
                # i + 1:
                # We cannot choose i again.
                #
                # k - 1:
                # We've just selected one number, so one fewer
                # number remains to be selected.
                # =================================================
                backtrack(i + 1, k - 1)

                # =================================================
                # UNDO
                #
                # Remove i so that the next iteration can try
                # another number.
                # =================================================
                path.pop()

        # Start choosing from 1.
        backtrack(1, k)

        return result
        