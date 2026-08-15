class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        i = len(s) - 1
         # Step 1:
        # Skip any spaces at the END of the string.
        #
        # Example:
        #
        # "Hello World   "
        #            ↑
        #          start here
        #
        # We don't want to count these spaces.
        # ---------------------------------------------------------
        while i >= 0 and s[i] == ' ':
            i -= 1
        # Now we are at the last character of the last word.
        #
        # Keep moving backwards while we're still inside the word.
        length = 0
        while i >= 0 and s[i] != ' ' :
            length += 1
            i -= 1
        return length    
        