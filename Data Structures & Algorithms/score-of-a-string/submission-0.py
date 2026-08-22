class Solution:
    def scoreOfString(self, s: str) -> int:

        # Stores the total score.
        score = 0

        # Start from index 1 because we compare
        # each character with the character BEFORE it.
        #
        # Example:
        # "code"
        #
        # i = 1 → compare o with c
        # i = 2 → compare d with o
        # i = 3 → compare e with d
        for i in range(1, len(s)):

            # ord() gives the ASCII value of a character.
            #
            # abs() gives the absolute difference,
            # so the order does not matter.
            difference = abs(ord(s[i]) - ord(s[i - 1]))

            # Add this adjacent-character difference
            # to our total score.
            score += difference

        return score 