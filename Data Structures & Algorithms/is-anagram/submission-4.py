class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        count = {}
        for c in s: ## Count characters in first string
            count[c] = count.get(c, 0) + 1
        for j in t: # Remove frequencies using second string
            count[j] = count.get(j, 0) - 1

        for value in count.values():
            if value != 0: # If any frequency is not 0,
            # strings are not anagrams

                return False
        return True       
