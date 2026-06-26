class Solution:
    def asteroidCollision(self, asteroids):

        # Stack stores asteroids that are still alive
        stack = []

        # Process every asteroid one by one
        for asteroid in asteroids:

            # Assume current asteroid survives
            alive = True

            # Collision is possible only when:
            #
            # stack top is moving right (+)
            # current asteroid moving left (-)
            while alive and stack and stack[-1] > 0 and asteroid < 0:

                # -------------------------------
                # Case 1
                # Current asteroid is bigger
                #
                # Example:
                #
                # stack top = 5
                # current   = -10
                #
                # 5 explodes
                # -------------------------------
                if abs(asteroid) > stack[-1]:

                    stack.pop()

                    # Continue because current asteroid
                    # may collide again
                    continue

                # -------------------------------
                # Case 2
                # Equal size
                #
                # Both explode
                # -------------------------------
                elif abs(asteroid) == stack[-1]:

                    stack.pop()

                    alive = False

                # -------------------------------
                # Case 3
                # Stack asteroid is bigger
                #
                # Current asteroid dies
                # -------------------------------
                else:

                    alive = False

            # If asteroid survived every collision
            # store it
            if alive:
                stack.append(asteroid)

        return stack
        