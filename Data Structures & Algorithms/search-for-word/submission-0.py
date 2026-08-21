class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:

        rows = len(board)
        cols = len(board[0])

        # ------------------------------------------------
        # DFS / BACKTRACKING
        #
        # r, c = current cell
        # i    = current character of word we are trying
        # ------------------------------------------------
        def dfs(r, c, i):

            # ------------------------------------------------
            # BASE CASE
            #
            # If i reached the length of the word,
            # we have successfully matched every character.
            # ------------------------------------------------
            if i == len(word):
                return True

            # ------------------------------------------------
            # INVALID CELL CHECK
            #
            # We cannot go outside the board.
            # ------------------------------------------------
            if r < 0 or r >= rows or c < 0 or c >= cols:
                return False

            # ------------------------------------------------
            # CHARACTER CHECK
            #
            # The current board cell must match the character
            # we are currently looking for.
            #
            # Example:
            #
            # word = "CAT"
            # i = 1
            #
            # We need 'A'.
            #
            # If board[r][c] = 'B',
            # this path cannot work.
            # ------------------------------------------------
            if board[r][c] != word[i]:
                return False

            # ------------------------------------------------
            # Mark this cell as visited.
            #
            # '#' means:
            # "We are currently using this cell."
            #
            # This prevents us from using the same cell twice
            # in the current path.
            # ------------------------------------------------
            temp = board[r][c]
            board[r][c] = '#'

            # ------------------------------------------------
            # Move in all 4 possible directions.
            #
            # i + 1 means we are now searching for the
            # NEXT character of the word.
            # ------------------------------------------------
            found = (
                dfs(r + 1, c, i + 1) or    # DOWN
                dfs(r - 1, c, i + 1) or    # UP
                dfs(r, c + 1, i + 1) or    # RIGHT
                dfs(r, c - 1, i + 1)       # LEFT
            )

            # ------------------------------------------------
            # BACKTRACK
            #
            # Restore the original character.
            #
            # Why?
            #
            # This cell may be used in a DIFFERENT path.
            # ------------------------------------------------
            board[r][c] = temp

            return found

        # ------------------------------------------------
        # We can start the word from ANY cell.
        #
        # Therefore check every cell in the board.
        # ------------------------------------------------
        for r in range(rows):
            for c in range(cols):

                # Only start DFS if this cell matches
                # the first character of the word.
                if board[r][c] == word[0]:

                    if dfs(r, c, 0):
                        return True

        # We tried every possible starting position
        # and couldn't form the word.
        return False  