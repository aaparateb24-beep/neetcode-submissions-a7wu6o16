class NumMatrix:

    def __init__(self, matrix):

        # Number of rows
        rows = len(matrix)

        # Number of columns
        cols = len(matrix[0])

        # --------------------------------------------------
        # Create a prefix matrix that is one row and
        # one column larger than the original matrix.
        #
        # Extra row and column contain 0.
        #
        # This makes boundary cases much easier.
        # --------------------------------------------------
        self.prefix = [
            [0] * (cols + 1)
            for _ in range(rows + 1)
        ]

        # --------------------------------------------------
        # Build the 2D prefix sum.
        # --------------------------------------------------
        for i in range(1, rows + 1):

            for j in range(1, cols + 1):

                # Current matrix value
                current = matrix[i - 1][j - 1]

                # Everything above
                top = self.prefix[i - 1][j]

                # Everything to the left
                left = self.prefix[i][j - 1]

                # Top-left area was counted twice,
                # so subtract it once.
                top_left = self.prefix[i - 1][j - 1]

                self.prefix[i][j] = (
                    current
                    + top
                    + left
                    - top_left
                )

    def sumRegion(self, row1, col1, row2, col2):

        # --------------------------------------------------
        # Start with the sum of the BIG rectangle
        # from (0,0) to (row2,col2).
        # --------------------------------------------------
        total = self.prefix[row2 + 1][col2 + 1]

        # --------------------------------------------------
        # Remove the part ABOVE our required rectangle.
        # --------------------------------------------------
        top = self.prefix[row1][col2 + 1]

        # --------------------------------------------------
        # Remove the part to the LEFT of our rectangle.
        # --------------------------------------------------
        left = self.prefix[row2 + 1][col1]

        # --------------------------------------------------
        # The top-left corner was removed twice.
        #
        # Therefore, add it back once.
        # --------------------------------------------------
        corner = self.prefix[row1][col1]

        return total - top - left + corner