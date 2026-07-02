class Solution:
    def search(self, nums, target):

        # Search space starts from the
        # first element to the last element.
        left = 0
        right = len(nums) - 1

        # Continue while search space exists.
        while left <= right:

            # Middle index
            mid = (left + right) // 2

            # Target found.
            if nums[mid] == target:
                return mid

            # -------------------------------------
            # Check if LEFT HALF is sorted.
            #
            # Example:
            # [4,5,6,7,0,1,2]
            #
            # left = 4
            # mid  = 7
            #
            # Since 4 <= 7,
            # left half is sorted.
            # -------------------------------------
            if nums[left] <= nums[mid]:

                # ---------------------------------
                # Is target inside the sorted
                # left half?
                #
                # Example:
                #
                # left = 4
                # mid  = 7
                #
                # Target = 5
                #
                # 4 <= 5 < 7
                #
                # YES
                # ---------------------------------
                if nums[left] <= target < nums[mid]:

                    # Search left half.
                    right = mid - 1

                else:

                    # Target is not inside
                    # left half.
                    #
                    # Search right half.
                    left = mid + 1

            # -------------------------------------
            # Otherwise,
            # RIGHT HALF must be sorted.
            # -------------------------------------
            else:

                # ---------------------------------
                # Is target inside the sorted
                # right half?
                #
                # Example:
                #
                # mid = 0
                # right = 2
                #
                # Target = 1
                #
                # 0 < 1 <= 2
                #
                # YES
                # ---------------------------------
                if nums[mid] < target <= nums[right]:

                    # Search right half.
                    left = mid + 1

                else:

                    # Search left half.
                    right = mid - 1

        # Target not found.
        return -1