import math

class Solution:
    def minEatingSpeed(self, piles, h):
        left, right = 1, max(piles)

        while left < right:
            mid = (left + right) // 2

            time = 0
            for pile in piles:
                time += math.ceil(pile / mid)

            if time <= h:
                right = mid     # try smaller k
            else:
                left = mid + 1  # need bigger k

        return left
