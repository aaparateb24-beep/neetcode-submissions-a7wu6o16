class Solution:
    def findInMountainArray(self, target: int, mountainArr: 'MountainArray') -> int:

        n = mountainArr.length()

        # ==================================================
        # STEP 1: FIND THE PEAK
        # ==================================================

        left = 0
        right = n - 1

        while left < right:

            # Find middle
            mid = (left + right) // 2

            # If middle value is smaller than the next value,
            # we are still climbing upward.
            #
            # Example:
            #
            #       mid
            #        ↓
            # 1 3 5 7 9
            #       ↑
            #    next is bigger
            #
            # Therefore, the peak must be on the RIGHT.
            if mountainArr.get(mid) < mountainArr.get(mid + 1):

                left = mid + 1

            # Otherwise, we are on the descending side
            # OR mid itself is the peak.
            #
            # Therefore, keep mid and search LEFT.
            else:
                right = mid

        # When left == right, we found the peak.
        peak = left


        # ==================================================
        # STEP 2: BINARY SEARCH INCREASING SIDE
        # ==================================================

        left = 0
        right = peak

        while left <= right:

            mid = (left + right) // 2
            value = mountainArr.get(mid)

            if value == target:
                return mid

            # Increasing side behaves like a normal
            # sorted array.
            elif value < target:

                # Target is larger,
                # so move RIGHT.
                left = mid + 1

            else:

                # Target is smaller,
                # so move LEFT.
                right = mid - 1


        # ==================================================
        # STEP 3: BINARY SEARCH DECREASING SIDE
        # ==================================================

        left = peak + 1
        right = n - 1

        while left <= right:

            mid = (left + right) // 2
            value = mountainArr.get(mid)

            if value == target:
                return mid

            # IMPORTANT:
            #
            # This side is DECREASING.
            #
            # Example:
            #
            # 9 7 5 3 1
            #
            # If value is smaller than target,
            # we need to move LEFT to find bigger values.
            elif value < target:

                right = mid - 1

            else:

                # value > target
                #
                # Need a smaller value.
                # Move RIGHT.
                left = mid + 1


        # Target does not exist.
        return -1