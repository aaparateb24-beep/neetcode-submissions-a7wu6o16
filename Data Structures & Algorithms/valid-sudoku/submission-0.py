from collections import defaultdict

class Solution:
    def isValidSudoku(self, board):

        # Stores numbers present in each row
        rows = defaultdict(set)

        # Stores numbers present in each column
        cols = defaultdict(set)

        # Stores numbers present in each 3x3 box
        boxes = defaultdict(set)

        # Visit every cell
        for r in range(9):
            for c in range(9):

                # Current value
                value = board[r][c]

                # Ignore empty cells
                if value == ".":
                    continue

                # Find which 3x3 box
                box = (r // 3, c // 3)

                # Duplicate found?
                if (value in rows[r] or
                    value in cols[c] or
                    value in boxes[box]):

                    return False

                # Store value
                rows[r].add(value)
                cols[c].add(value)
                boxes[box].add(value)

        return True