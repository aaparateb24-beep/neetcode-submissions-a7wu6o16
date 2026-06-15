class Solution:
    def numRescueBoats(self, people, limit):

        # sort weights
        people.sort()

        # lightest person
        left = 0

        # heaviest person
        right = len(people) - 1

        boats = 0

        while left <= right:

            # can lightest and heaviest fit together?
            if people[left] + people[right] <= limit:

                # take both
                left += 1
                right -= 1

            else:

                # heaviest goes alone
                right -= 1

            # one boat used
            boats += 1

        return boats             

        
                
        