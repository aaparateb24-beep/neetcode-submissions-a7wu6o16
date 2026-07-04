class Solution:
    def splitArray(self, nums, k):

        # ---------------------------------------
        # The smallest possible answer is the
        # largest element.
        #
        # Example:
        # nums = [7,2,5,10,8]
        #
        # Largest element = 10
        #
        # We can never choose an answer
        # smaller than 10 because that
        # element itself must fit.
        # ---------------------------------------
        left = max(nums)

        # ---------------------------------------
        # The largest possible answer is
        # the sum of the entire array.
        #
        # Example:
        #
        # [7,2,5,10,8]
        #
        # Sum = 32
        #
        # This means we never split.
        # ---------------------------------------
        right = sum(nums)

        # Initially assume the worst answer.
        answer = right

        # Binary Search
        while left <= right:

            # Guess the maximum allowed
            # subarray sum.
            mid = (left + right) // 2

            # ----------------------------
            # Helper variables
            #
            # We always start with
            # one partition.
            # ----------------------------
            partitions = 1

            # Current sum inside
            # the current partition.
            current_sum = 0

            # ---------------------------------
            # Try creating partitions
            # where every partition sum
            # is <= mid.
            # ---------------------------------
            for num in nums:

                # Can current number fit
                # into the current partition?
                if current_sum + num <= mid:

                    # Yes.
                    # Keep adding.
                    current_sum += num

                else:

                    # No.
                    #
                    # Start a new partition.
                    partitions += 1

                    # Current number becomes
                    # the first element of
                    # the new partition.
                    current_sum = num

            # ----------------------------------
            # If required partitions are
            # less than or equal to k,
            # then this maximum sum works.
            # ----------------------------------
            if partitions <= k:

                # Save this answer.
                answer = mid

                # Try finding an even
                # smaller maximum sum.
                right = mid - 1

            else:

                # Too many partitions.
                #
                # Our guessed maximum sum
                # is too small.
                #
                # Increase it.
                left = mid + 1

        # Smallest possible largest sum.
        return answer
        