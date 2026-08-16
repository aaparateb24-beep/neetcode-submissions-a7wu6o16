class Solution:
    def combine(self, n: int, k: int):

        path = []
        result = []

        def backtrack(start, k):

            # We have selected exactly k numbers.
            if k == 0:
                result.append(path.copy())
                return

            for i in range(start, n + 1):
                path.append(i)

                # Choose the next number.
                backtrack(i + 1, k - 1)

                # Undo the choice.
                path.pop()

        backtrack(1, k)

        return result   
                
        