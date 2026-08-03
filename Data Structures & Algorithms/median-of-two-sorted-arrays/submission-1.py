class Solution:
    def findMedianSortedArrays(self, nums1, nums2):

        # ----------------------------------------------------
        # We ALWAYS perform binary search on the SMALLER array.
        #
        # Why?
        # Binary Search complexity depends on the size of the
        # array we're searching.
        #
        # Searching the smaller array gives
        # O(log(min(m,n))).
        #
        # If nums1 is larger, simply swap them.
        # ----------------------------------------------------
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1

        # Lengths of both arrays
        m = len(nums1)
        n = len(nums2)

        # Total number of elements.
        total = m + n

        # Number of elements that should be present
        # in the LEFT half.
        #
        # Example:
        #
        # total = 5
        #
        # Left = 3
        # Right = 2
        #
        # total = 6
        #
        # Left = 3
        # Right = 3
        #
        # Formula works for both odd and even.
        half = (total + 1) // 2

        # Binary Search boundaries
        low = 0
        high = m

        # Continue Binary Search
        while low <= high:

            # ---------------------------------------------
            # Choose where to CUT the first array.
            #
            # Example
            #
            # nums1
            #
            # 1 3 8 9
            #
            # partition1 = 2
            #
            # 1 3 | 8 9
            # ---------------------------------------------
            partition1 = (low + high) // 2

            # ---------------------------------------------
            # Automatically calculate where to cut
            # the second array.
            #
            # Why?
            #
            # Because the LEFT half should always contain
            # exactly 'half' elements.
            #
            # If partition1 contributes some elements,
            # partition2 contributes the remaining.
            # ---------------------------------------------
            partition2 = half - partition1

            # -------------------------------------------------
            # Find the LAST element on the LEFT side
            # of nums1.
            #
            # If partition1 == 0,
            # there is nothing on the left.
            #
            # We imagine
            #
            # Left1 = -∞
            #
            # so comparisons always work.
            # -------------------------------------------------
            if partition1 == 0:
                left1 = float("-inf")
            else:
                left1 = nums1[partition1 - 1]

            # -------------------------------------------------
            # Find the FIRST element on the RIGHT side
            # of nums1.
            #
            # If partition reaches the end,
            # nothing exists on the right.
            #
            # Imagine
            #
            # Right1 = +∞
            # -------------------------------------------------
            if partition1 == m:
                right1 = float("inf")
            else:
                right1 = nums1[partition1]

            # Same idea for nums2

            if partition2 == 0:
                left2 = float("-inf")
            else:
                left2 = nums2[partition2 - 1]

            if partition2 == n:
                right2 = float("inf")
            else:
                right2 = nums2[partition2]

            # ------------------------------------------------
            # VERY IMPORTANT CHECK
            #
            # We have found the correct partition ONLY IF
            #
            # Largest element of Left1
            # <=
            # Smallest element of Right2
            #
            # AND
            #
            # Largest element of Left2
            # <=
            # Smallest element of Right1
            #
            # Why?
            #
            # Because then ALL elements on the left
            # are smaller than ALL elements on the right.
            #
            # That means the partition is perfect.
            # ------------------------------------------------
            if left1 <= right2 and left2 <= right1:

                # ------------------------------------------
                # ODD number of elements.
                #
                # Example
                #
                # 1 2 3 | 4 5
                #
                # Median is simply the largest value
                # on the LEFT.
                # ------------------------------------------
                if total % 2 == 1:
                    return max(left1, left2)

                # ------------------------------------------
                # EVEN number of elements.
                #
                # Example
                #
                # 1 2 | 3 4
                #
                # Middle elements are
                #
                # Largest Left
                #
                # Smallest Right
                #
                # Average them.
                # ------------------------------------------
                return (
                    max(left1, left2) +
                    min(right1, right2)
                ) / 2.0

            # ------------------------------------------------
            # Suppose
            #
            # Left1 > Right2
            #
            # Example
            #
            # nums1
            #
            # 5 | 8
            #
            # nums2
            #
            # 1 2 3 |
            #
            # Here
            #
            # Left1 = 5
            #
            # Right2 = 3
            #
            # 5 > 3
            #
            # Too many elements have been taken
            # from nums1.
            #
            # Move partition LEFT.
            # ------------------------------------------------
            elif left1 > right2:
                high = partition1 - 1

            # ------------------------------------------------
            # Otherwise
            #
            # Left2 > Right1
            #
            # Example
            #
            # nums1
            #
            # | 2
            #
            # nums2
            #
            # 1 3 |
            #
            # Left2 = 3
            #
            # Right1 = 2
            #
            # 3 > 2
            #
            # We have taken TOO FEW elements
            # from nums1.
            #
            # Move partition RIGHT.
            # ------------------------------------------------
            else:
                low = partition1 + 1