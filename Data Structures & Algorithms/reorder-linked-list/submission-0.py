class Solution:
    def reorderList(self, head):
        # Step 1: find middle
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # Step 2: reverse second half
        prev = None
        curr = slow.next
        slow.next = None

        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt

        # Step 3: merge
        first = head
        second = prev

        while second:
            temp1 = first.next
            temp2 = second.next

            first.next = second
            second.next = temp1

            first = temp1
            second = temp2