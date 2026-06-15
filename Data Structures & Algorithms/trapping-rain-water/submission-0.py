class Solution:
    def trap(self, height):

        # start from both ends
        left = 0
        right = len(height) - 1

        # highest wall seen from left side
        left_max = 0

        # highest wall seen from right side
        right_max = 0

        # total trapped water
        water = 0

        while left < right:

            # update highest wall seen so far from left
            left_max = max(left_max, height[left])

            # update highest wall seen so far from right
            right_max = max(right_max, height[right])

            # if left side is the smaller boundary
            if left_max < right_max:

                # water at current left building
                # = boundary height - building height
                water += left_max - height[left]

                # move left pointer
                left += 1

            # if right side is the smaller boundary
            else:

                # water at current right building
                water += right_max - height[right]

                # move right pointer
                right -= 1

        return water
        