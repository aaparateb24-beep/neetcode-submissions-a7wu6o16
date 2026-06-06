class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        target = sorted(s1)
        for i in range(len(s2) - len(s1) + 1):
            # Current window
            window = s2[i:i + len(s1)]

            # Compare sorted characters
            if sorted(window) == target:
                return True

        return False