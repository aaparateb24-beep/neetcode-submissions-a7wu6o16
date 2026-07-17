class Solution:
    def reorderList(self, head):

        # Edge case
        if not head or not head.next:
            return

        # -----------------------------
        # Step 1 : Find Middle
        # -----------------------------
        slow = head
        fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # -----------------------------
        # Step 2 : Reverse second half
        # -----------------------------
        prev = None
        curr = slow.next

        # Cut the list into two halves
        slow.next = None

        while curr:

            nxt = curr.next

            curr.next = prev

            prev = curr

            curr = nxt

        # prev is the head of reversed second half

        # -----------------------------
        # Step 3 : Merge both halves
        # -----------------------------
        first = head
        second = prev

        while second:

            temp1 = first.next
            temp2 = second.next

            first.next = second
            second.next = temp1

            first = temp1
            second = temp2
        