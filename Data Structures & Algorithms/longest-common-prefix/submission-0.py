class Solution:
    def longestCommonPrefix(self, strs):
        # Edge case
        if not strs:
            return ""

        result = ""

        # Iterate through characters of first string
        for i in range(len(strs[0])):
            current_char = strs[0][i]

            # Compare with same index in other strings
            for j in range(1, len(strs)):
                if i >= len(strs[j]) or strs[j][i] != current_char:
                    return result

            result += current_char

        return result



