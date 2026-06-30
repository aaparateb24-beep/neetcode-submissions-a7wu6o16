class Solution:
    def shipWithinDays(self, weights, days):

        # ---------------------------------------
        # Minimum possible capacity
        #
        # Ship must at least carry
        # the heaviest package.
        #
        # Example:
        # weights = [2,5,10]
        #
        # Capacity cannot be 8
        # because package 10
        # cannot even fit.
        # ---------------------------------------
        left = max(weights)

        # ---------------------------------------
        # Maximum possible capacity
        #
        # Ship carries every package
        # in one day.
        # ---------------------------------------
        right = sum(weights)

        # Store minimum valid capacity
        answer = right

        # ---------------------------------------
        # Binary Search
        # ---------------------------------------
        while left <= right:

            # Current capacity
            mid = (left + right) // 2

            # We always need
            # at least one day.
            current_days = 1

            # Current ship load
            current_weight = 0

            # ---------------------------------------
            # Try shipping packages
            # with capacity = mid
            # ---------------------------------------
            for weight in weights:

                # If package fits
                if current_weight + weight <= mid:

                    # Put package
                    # into today's ship.
                    current_weight += weight

                else:

                    # Ship is full.
                    #
                    # Start next day.
                    current_days += 1

                    # First package
                    # of new day.
                    current_weight = weight

            # ---------------------------------------
            # Finished simulation.
            #
            # Can we ship
            # within required days?
            # ---------------------------------------
            if current_days <= days:

                # YES
                #
                # Capacity works.
                answer = mid

                # Try smaller capacity.
                right = mid - 1

            else:

                # NO
                #
                # Capacity too small.
                left = mid + 1

        return answer
        