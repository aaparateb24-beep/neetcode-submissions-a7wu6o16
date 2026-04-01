from typing import List, Dict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups: Dict[tuple, List[str]] = {}

        for s in strs:
            # signature: a tuple of 26 counts for 'a'..'z'
            count = [0] * 26
            for ch in s:
                count[ord(ch) - ord('a')] += 1
            key = tuple(count)

            if key not in groups:
                groups[key] = []
            groups[key].append(s)

        return list(groups.values())
