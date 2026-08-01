class Solution:
    def findContentChildren(self, g, s):

        # Sort children by greed
        g.sort()

        # Sort cookies by size
        s.sort()

        # Pointer for children
        child = 0

        # Pointer for cookies
        cookie = 0

        # Number of satisfied children
        satisfied = 0

        # Continue while both arrays
        # still have elements.
        while child < len(g) and cookie < len(s):

            # Current cookie is big enough
            # for current child.
            if s[cookie] >= g[child]:

                # Child becomes satisfied.
                satisfied += 1

                # Move to next child.
                child += 1

                # Current cookie is used.
                cookie += 1

            else:

                # Cookie is too small.
                #
                # It cannot satisfy this child
                # or any greedier child.
                #
                # Discard this cookie.
                cookie += 1

        return satisfied
        