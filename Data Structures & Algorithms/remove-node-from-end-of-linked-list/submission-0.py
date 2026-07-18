# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
         # -------------------------------------------------------
        # Step 1: Create a dummy node.
        #
        # Why?
        # Suppose we need to remove the head itself.
        #
        # Example:
        # 1 -> 2 -> 3
        # n = 3
        #
        # Without a dummy node, deleting the head becomes a special case.
        # With a dummy node, every deletion is handled the same way.
        # ------------------------------------------------------
        dummy = ListNode(0)
        dummy.next = head
        fast = dummy 
        slow = dummy 
        # -------------------------------------------------------
        # Step 2: Move the fast pointer (n + 1) steps ahead.
        #
        # Why n+1?
        #
        # We want the slow pointer to stop ONE NODE BEFORE
        # the node we want to delete.
        #
        # Example:
        #
        # D -> 1 -> 2 -> 3 -> 4 -> 5
        # Remove 4 (n = 2)
        #
        # After moving fast 3 steps:
        #
        # slow = D
        # fast = 3
        #
        # Now the gap between slow and fast is exactly 3 nodes.
        # -------------------------------------------------------
        for _ in range(n +1):
            fast = fast.next 
            # Step 3: Move both pointers together.
        #
        # Since the gap never changes,
        # when fast reaches the end,
        # slow will be exactly ONE NODE BEFORE
        # the node we need to remove.
        # -------------------------------------------------------
        while fast:

            slow = slow.next
            fast = fast.next

        # -------------------------------------------------------
        # Step 4: Delete the target node.
        #
        # Current situation:
        #
        # slow
        #   ↓
        # 3 -> 4 -> 5
        #
        # We don't move or delete node 4 directly.
        #
        # Instead,
        #
        # make 3 point to 5.
        #
        # 3 ------------> 5
        #
        # Node 4 is skipped.
        # -------------------------------------------------------
        slow.next = slow.next.next 
        # -------------------------------------------------------
        # Step 5:
        #
        # The real head starts after the dummy node.
        # -------------------------------------------------------
        return dummy.next 