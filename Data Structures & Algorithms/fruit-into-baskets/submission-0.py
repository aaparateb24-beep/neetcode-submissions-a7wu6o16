class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        
        

        # left side of window
        left = 0

        # fruit frequency map
        count = {}

        # answer
        longest = 0

        # right expands window
        for right in range(len(fruits)):

            fruit = fruits[right]

            # add fruit into window
            count[fruit] = count.get(fruit, 0) + 1

            # too many fruit types
            while len(count) > 2:

                left_fruit = fruits[left]

                # remove left fruit
                count[left_fruit] -= 1

                # frequency becomes 0
                # remove from map
                if count[left_fruit] == 0:
                    del count[left_fruit]

                left += 1

            # current valid window size
            current_length = right - left + 1

            longest = max(longest, current_length)

        return longest

        