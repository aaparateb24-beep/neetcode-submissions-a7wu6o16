class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = set() #hashset
        left = 0 #left side of window
        max_len = 0 #best found ans so far 

        for right in range(len(s)): 
            while s[right] in seen: #duplicate found
                seen.remove(s[left]) #shrink 
                left += 1
            seen.add(s[right])     #expand else
            curr_len = right - left +1 
            max_len = max(curr_len, max_len)   
        return max_len       