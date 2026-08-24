class Solution:
    def construct(self, grid):

        n = len(grid)

        def build(row, col, size):

            # ---------------------------------------------
            # CHECK WHETHER THE CURRENT SQUARE IS UNIFORM
            #
            # We take the first cell as the expected value.
            # Then check every other cell.
            # ---------------------------------------------
            value = grid[row][col]

            for r in range(row, row + size):
                for c in range(col, col + size):

                    # If we find a different value,
                    # this square is NOT uniform.
                    if grid[r][c] != value:

                        # Stop checking.
                        # We know we need to divide this square.
                        break

                else:
                    # Inner loop finished without break.
                    continue

                # Inner loop was broken.
                break

            else:
                # BOTH loops finished normally.
                #
                # Therefore every cell had the same value.
                #
                # Create a leaf node.
                return Node(
                    value == 1,
                    True,
                    None,
                    None,
                    None,
                    None
                )

            # ---------------------------------------------
            # CURRENT REGION HAS BOTH 0 AND 1.
            #
            # Therefore it cannot be a leaf.
            # ---------------------------------------------

            half = size // 2

            # Create a non-leaf node.
            node = Node(
                True,
                False,
                None,
                None,
                None,
                None
            )

            # ---------------------------------------------
            # DIVIDE INTO 4 QUADRANTS
            # ---------------------------------------------

            # Top Left
            node.topLeft = build(
                row,
                col,
                half
            )

            # Top Right
            node.topRight = build(
                row,
                col + half,
                half
            )

            # Bottom Left
            node.bottomLeft = build(
                row + half,
                col,
                half
            )

            # Bottom Right
            node.bottomRight = build(
                row + half,
                col + half,
                half
            )

            return node

        # Start with the entire grid.
        return build(0, 0, n)
