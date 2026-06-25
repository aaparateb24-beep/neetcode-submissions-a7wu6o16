class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:

        # -------------------------------------------------------
        # Step 1:
        # Pair every car's position with its speed.
        #
        # Example:
        # position = [10,8,0]
        # speed    = [2,4,1]
        #
        # cars = [(10,2), (8,4), (0,1)]
        # -------------------------------------------------------
        cars = list(zip(position, speed))

        # -------------------------------------------------------
        # Step 2:
        # Sort cars according to position.
        #
        # We want to process cars from nearest to target
        # towards the farthest.
        # -------------------------------------------------------
        cars.sort()

        # -------------------------------------------------------
        # Stack stores arrival times of fleets.
        #
        # Example:
        # stack = [1.0, 7.0]
        #
        # Means:
        # Fleet 1 reaches in 1 hour
        # Fleet 2 reaches in 7 hours
        # -------------------------------------------------------
        stack = []

        # -------------------------------------------------------
        # Traverse from right to left.
        #
        # Why?
        #
        # Because the car nearest the target
        # cannot be affected by anyone in front.
        #
        # It becomes our first fleet.
        # -------------------------------------------------------
        for pos, spd in reversed(cars):

            # ---------------------------------------------------
            # Calculate time required to reach target.
            #
            # Formula:
            #
            # distance / speed
            #
            # Example:
            #
            # Target = 12
            # Position = 10
            # Speed = 2
            #
            # Time = (12-10)/2 = 1
            # ---------------------------------------------------
            time = (target - pos) / spd

            # ---------------------------------------------------
            # Put this car's arrival time into stack.
            #
            # Initially assume it forms a new fleet.
            # ---------------------------------------------------
            stack.append(time)

            # ---------------------------------------------------
            # Now compare with fleet in front.
            #
            # If current car reaches EARLIER
            # than fleet ahead,
            #
            # it catches that fleet.
            #
            # Example:
            #
            # Current car time = 1
            # Fleet ahead time = 2
            #
            # Since 1 <= 2
            #
            # Current car catches fleet ahead.
            #
            # They become ONE fleet.
            # ---------------------------------------------------
            if len(stack) >= 2 and stack[-1] <= stack[-2]:

                # -----------------------------------------------
                # Remove current time.
                #
                # Why?
                #
                # Because current car merges
                # into previous fleet.
                #
                # We only keep arrival time
                # of merged fleet.
                # -----------------------------------------------
                stack.pop()

        # -------------------------------------------------------
        # Number of remaining times
        # equals number of fleets.
        # -------------------------------------------------------
        return len(stack)
        