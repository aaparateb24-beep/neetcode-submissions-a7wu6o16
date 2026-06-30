class Solution:
    def minEatingSpeed(self, piles, h):

        left = 1
        right = max(piles)

        answer = right

        while left <= right:

            mid = (left + right) // 2

            total_hours = 0

            for pile in piles:

                # Same as ceil(pile / mid)
                total_hours += (pile + mid - 1) // mid

            if total_hours <= h:

                answer = mid
                right = mid - 1

            else:

                left = mid + 1

        return answer
        