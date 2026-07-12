class Solution:
    def numIslands(self, grid):

        # Number of rows in the grid
        rows = len(grid)

        # Number of columns in the grid
        cols = len(grid[0])

        # ---------------------------------------------------------
        # DFS Function
        #
        # Purpose:
        # Starting from ONE land cell,
        # visit EVERY connected land cell
        # and mark it as visited.
        #
        # Think of it like:
        # "Walk through the whole island."
        # ---------------------------------------------------------
        def dfs(r, c):

            # -------------------------
            # Base Case 1
            #
            # If we go outside the grid,
            # stop exploring.
            # -------------------------
            if r < 0 or c < 0 or r >= rows or c >= cols:
                return

            # -------------------------
            # Base Case 2
            #
            # If current cell is water
            # OR already visited,
            # stop exploring.
            #
            # We mark visited cells as '0',
            # so both water and visited
            # are treated the same.
            # -------------------------
            if grid[r][c] == "0":
                return

            # -------------------------
            # We found land.
            #
            # Mark it as visited so
            # we don't count it again.
            #
            # 1 ---> 0
            # -------------------------
            grid[r][c] = "0"

            # -------------------------------------------------
            # Now explore all 4 neighbours.
            #
            # Every neighbour again performs
            # the SAME DFS.
            #
            # This continues until
            # no more land is connected.
            # -------------------------------------------------

            # Down
            dfs(r + 1, c)

            # Up
            dfs(r - 1, c)

            # Right
            dfs(r, c + 1)

            # Left
            dfs(r, c - 1)

        # ------------------------------------
        # Stores answer.
        #
        # Every time we discover
        # a NEW island,
        # we'll increment it.
        # ------------------------------------
        islands = 0

        # ------------------------------------
        # Scan every cell of the grid.
        #
        # Think:
        # "Let's search the whole map."
        # ------------------------------------
        for r in range(rows):
            for c in range(cols):

                # --------------------------------
                # If current cell is land,
                # this means we discovered
                # a NEW island.
                # --------------------------------
                if grid[r][c] == "1":

                    # Count this island
                    islands += 1

                    # Remove (visit) the ENTIRE island
                    #
                    # After DFS finishes,
                    # every connected '1'
                    # becomes '0'.
                    dfs(r, c)

        # Return total islands found
        return islands