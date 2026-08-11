class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
         # Deque stores INDICES, not actual values.
        #
        # We maintain the deque so that the values
        # are always in decreasing order.
        #
        # Therefore:
        # deque[0] → index of the maximum element
        from collections import deque
        q = deque()
        # Stores the maximum of every window.
        result = []

        for i in range(len(nums)):

         
            # STEP 1:
            # Remove elements that are OUTSIDE the window.
            # Current window starts at:
            # i - k + 1
            #
            # Therefore an index <= i-k is no longer valid.
            while q and q[0] <= i - k:
                q.popleft()
            # Remove smaller elements from the BACK.
            #
            # Suppose deque contains:
            #
            # [3, 2, 1]
            #
            # Current number is 5.
            #
            # Since 5 is greater than all of them,
            # none of 3,2,1 can ever become maximum
            # while 5 is inside the window.
            #
            # So remove them.
            while q and nums[i] > nums[q[-1]]:
                q.pop()
            q.append(i)        
           # Once we have at least k elements,
            # the window is complete.
            #
            # The FRONT of deque is always the index
            # of the largest element.
            if i >= k - 1:
                result.append(nums[q[0]])
        return result         