class Solution:
    def makesquare(self, matchsticks: List[int]) -> bool:

        # A square has 4 equal sides.
        # So we need at least 4 matchsticks.
        if len(matchsticks) < 4:
            return False
        # Calculate the total length of all matchsticks.
        total = sum(matchsticks)
        # The total must be divisible by 4.
        #
        # Example:
        # total = 10
        #
        # 10 / 4 is not an integer,
        # so 4 equal sides are impossible.
        if total % 4 != 0:
            return False

        # Every side must have this length.
        target = total // 4
        # Put larger matchsticks first.
        #
        # This helps us discover impossible arrangements
        # earlier and makes backtracking faster.
        matchsticks.sort(reverse=True)

        # Length currently placed on each of the 4 sides.
        sides = [0, 0, 0, 0]
        
        def backtrack(index):

            # ---------------------------------------------
            # BASE CASE
            #
            # If every matchstick has been placed,
            # then all four sides must have reached target.
            # ---------------------------------------------
            if index == len(matchsticks):
                return True

            # Take the current matchstick.
            stick = matchsticks[index]
            # Try putting this matchstick on each of the
            # four sides.
            # ---------------------------------------------
            for i in range(4):

                # If adding this stick makes the side
                # larger than the required target,
                # this choice cannot work.
                if sides[i] + stick > target:
                    continue

                # CHOOSE
                # Put the stick on this side.
                sides[i] += stick

                # RECURSE
                # Try placing the remaining matchsticks.
                if backtrack(index + 1):
                    return True
                # BACKTRACK / UNDO
                # Remove the stick because this arrangement
                # did not lead to a solution.
                sides[i] -= stick

            # We tried all 4 sides and none worked.
            return False

        return backtrack(0)    
    