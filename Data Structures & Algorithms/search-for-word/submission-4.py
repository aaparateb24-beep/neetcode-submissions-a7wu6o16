class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:

        rows = len(board)
        cols = len(board[0])

        def dfs(r, c, i):

            # -----------------------------------------
            # 1. CHECK IF WE ARE OUTSIDE THE BOARD
            # -----------------------------------------
            if r < 0 or r >= rows or c < 0 or c >= cols:
                return False

            # -----------------------------------------
            # 2. CHECK IF CURRENT CHARACTER IS WRONG
            # -----------------------------------------
            if board[r][c] != word[i]:
                return False

            # -----------------------------------------
            # 3. IF THIS WAS THE LAST CHARACTER,
            #    WE FOUND THE WORD
            # -----------------------------------------
            if i == len(word) - 1:
                return True

            # -----------------------------------------
            # 4. MARK CURRENT CELL AS VISITED
            # -----------------------------------------
            temp = board[r][c]
            board[r][c] = '#'

            # -----------------------------------------
            # 5. TRY ALL 4 DIRECTIONS
            # -----------------------------------------
            found = (
                dfs(r + 1, c, i + 1) or  # DOWN
                dfs(r - 1, c, i + 1) or  # UP
                dfs(r, c + 1, i + 1) or  # RIGHT
                dfs(r, c - 1, i + 1)      # LEFT
            )

            # -----------------------------------------
            # 6. BACKTRACK
            #    Restore the original character.
            # -----------------------------------------
            board[r][c] = temp

            return found

        # -----------------------------------------
        # TRY EVERY CELL AS A STARTING POINT
        # -----------------------------------------
        for r in range(rows):
            for c in range(cols):

                if board[r][c] == word[0]:

                    if dfs(r, c, 0):
                        return True

        return False