class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:

        # If s1 is bigger, impossible
        if len(s1) > len(s2):
            return False

        # Frequency map of s1
        need = {}

        for char in s1:
            need[char] = need.get(char, 0) + 1

        # Check every window of size len(s1)
        for i in range(len(s2) - len(s1) + 1):

            # Build current window frequency map
            window = {}

            for j in range(i, i + len(s1)):
                window[s2[j]] = window.get(s2[j], 0) + 1

            # If maps match, permutation found
            if window == need:
                return True

        return False
        