class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        result = [0] * len(temperatures)   
        stack = []
        for i , temp in enumerate(temperatures):
            while stack and temp > stack[-1][0]:

                # Previous day waiting for answer
                prev_temp, prev_index = stack.pop()

                # Days waited
                #
                # Example:
                # prev_index = 3
                # current i = 5
                #
                # waited = 5 - 3 = 2
                result[prev_index] = i - prev_index

             # Current day now waits
            # for its future warmer day
            stack.append((temp, i))

        # Remaining stack elements
        # never found a warmer day
        #
        # Their answer remains 0
        return result         