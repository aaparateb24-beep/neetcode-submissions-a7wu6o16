class Solution:
    def minWindow(self, s: str, t: str) -> str:

        # Frequency map of characters we need
        need_count = {}

        for char in t:
            need_count[char] = need_count.get(char, 0) + 1

        # Frequency map of current window
        window_count = {}

        # Number of satisfied requirements
        have = 0

        # Total unique requirements
        need = len(need_count)

        left = 0

        # Store best answer
        result_start = 0
        result_length = float("inf")

        # Expand window
        for right in range(len(s)):

            char = s[right]

            # Add incoming character
            window_count[char] = window_count.get(char, 0) + 1

            # Requirement satisfied?
            if (
                char in need_count
                and window_count[char] == need_count[char]
            ):
                have += 1

            # Window valid
            while have == need:

                # Update smallest answer
                current_length = right - left + 1

                if current_length < result_length:
                    result_length = current_length
                    result_start = left

                # Character leaving window
                left_char = s[left]

                window_count[left_char] -= 1

                # Requirement broken?
                if (
                    left_char in need_count
                    and window_count[left_char] < need_count[left_char]
                ):
                    have -= 1

                left += 1

        # No valid window found
        if result_length == float("inf"):
            return ""

        return s[result_start : result_start + result_length]
        