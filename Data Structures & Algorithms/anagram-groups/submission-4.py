from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs):

        # Dictionary where:
        #
        # Key   -> Sorted version of word
        # Value -> List of original words
        #
        # Example:
        #
        # "aet" -> ["eat","tea","ate"]
        groups = defaultdict(list)

        # Visit every word
        for word in strs:

            # Sort all letters
            #
            # Example:
            # "tea"
            #
            # becomes
            #
            # ['a','e','t']
            sorted_word = sorted(word)

            # Convert list back into string
            #
            # ['a','e','t']
            #
            # becomes
            #
            # "aet"
            key = "".join(sorted_word)

            # Store original word
            # under its sorted key
            groups[key].append(word)

        # Return only grouped lists
        return list(groups.values())