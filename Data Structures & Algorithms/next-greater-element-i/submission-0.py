class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        # Stores next greater element
        nextGreater = {}

        # Monotonic decreasing stack
        stack = []

        # Traverse nums2
        for num in nums2:

            # If current number is greater
            # than the top of the stack,
            # then we found the next greater
            # element for the stack top.
            while stack and num > stack[-1]:
                smaller = stack.pop()

                nextGreater[smaller] = num

            # Current number still doesn't
            # know its next greater element.
            # Keep it in the stack.
            stack.append(num)

        # Remaining numbers never found
        # a greater element.
        while stack:
            nextGreater[stack.pop()] = -1

        # Build answer for nums1
        answer = []

        for num in nums1:
            answer.append(nextGreater[num])

        return answer