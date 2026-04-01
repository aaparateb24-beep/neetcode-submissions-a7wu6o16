class Solution:
    def searchMatrix(self, matrix, target):
        m, n = len(matrix), len(matrix[0])   # rows and columns

        left, right = 0, m * n - 1           # treat as 1D array

        while left <= right:
            mid = (left + right) // 2        # middle index

            row = mid // n                  # convert to row
            col = mid % n                  # convert to column

            val = matrix[row][col]          # get value

            if val == target:
                return True
            elif val < target:
                left = mid + 1              # search right half
            else:
                right = mid - 1             # search left half

        return False