class Solution:
    def isPalindrome(self, head):

        # ------------------------------
        # Step 1:
        # Find the middle of the linked list.
        # ------------------------------
        slow = head
        fast = head

        while fast and fast.next:

            # Slow moves one step.
            slow = slow.next

            # Fast moves two steps.
            fast = fast.next.next

        # ------------------------------
        # Step 2:
        # Reverse the second half
        # starting from the middle.
        # ------------------------------
        prev = None
        curr = slow

        while curr:

            # Save next node.
            nxt = curr.next

            # Reverse pointer.
            curr.next = prev

            # Move prev forward.
            prev = curr

            # Move curr forward.
            curr = nxt

        # 'prev' is now the head
        # of the reversed second half.
        second = prev

        # First pointer starts
        # from the beginning.
        first = head

        # ------------------------------
        # Step 3:
        # Compare both halves.
        # ------------------------------
        while second:

            # Values must be equal.
            if first.val != second.val:
                return False

            # Move both pointers.
            first = first.next
            second = second.next

        # All values matched.
        return True