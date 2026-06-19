class Solution:
    def characterReplacement(self, s, k):

        # Left side of window
        left = 0

        # Frequency of characters inside current window
        count = {}

        # Highest frequency character seen in current window
        max_freq = 0

        # Best answer found so far
        longest = 0

        # Right pointer expands window
        for right in range(len(s)):

            # Current character entering window
            char = s[right]

            # Add character to frequency map
            count[char] = count.get(char, 0) + 1

            # Update highest frequency character
            max_freq = max(max_freq, count[char])

            # ------------------------------------------------
            # Replacements needed
            #
            # window size - most frequent character count
            #
            # Example:
            # AABAB
            #
            # window size = 5
            # max_freq = 3 (A appears 3 times)
            #
            # replacements needed = 5 - 3 = 2
            # ------------------------------------------------

            while (right - left + 1) - max_freq > k:

                # Character leaving window
                left_char = s[left]

                # Reduce its count
                count[left_char] -= 1

                # Shrink window
                left += 1

            # Current valid window size
            current_length = right - left + 1

            # Update answer
            longest = max(longest, current_length)

        return longest
        