# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
         # ---------------------------------------------------------
        # STEP 1:
        # Create a dummy node.
        #
        # Why?
        # We don't know yet which node (list1 or list2)
        # will become the head of our merged linked list.
        #
        # The dummy node acts as a temporary starting point.
        #
        # Example:
        #
        # dummy
        #   ↓
        #  0 → None
        # ---------------------------------------------------------
        dummy = ListNode()

        # ---------------------------------------------------------
        # STEP 2:
        # 'tail' always points to the LAST node
        # of the merged linked list.
        #
        # Initially:
        #
        # dummy
        #   ↑
        # tail
        # ---------------------------------------------------------
        tail = dummy
         # ---------------------------------------------------------
        # STEP 3:
        # Continue until one of the linked lists finishes.
        #
        # If either list becomes empty,
        # we stop comparing.
        # ---------------------------------------------------------
        while list1 and list2:

            # -----------------------------------------------------
            # Compare current nodes.
            #
            # Always take the smaller node
            # because both linked lists are already sorted.
            # -----------------------------------------------------
            if list1.val < list2.val:

                # ---------------------------------------------
                # Attach the smaller node
                # to the merged linked list.
                #
                # Example:
                #
                # tail → 1
                # ---------------------------------------------
                tail.next = list1

                # ---------------------------------------------
                # Move list1 forward
                # because we already used its current node.
                # ---------------------------------------------
                list1 = list1.next

            else:

                # ---------------------------------------------
                # list2 is smaller (or equal),
                # so attach it.
                # ---------------------------------------------
                tail.next = list2

                # Move list2 forward.
                list2 = list2.next

            # -----------------------------------------------------
            # IMPORTANT
            #
            # Move tail forward.
            #
            # Why?
            #
            # Because the node we just attached
            # becomes the new last node.
            # -----------------------------------------------------
            tail = tail.next

        # ---------------------------------------------------------
        # STEP 4
        #
        # One linked list may still have nodes left.
        #
        # Example:
        #
        # list1 finished
        #
        # list2:
        #
        # 8 → 10 → 15
        #
        # They are already sorted,
        # so attach the entire remaining list.
        # ---------------------------------------------------------
        if list1:
            tail.next = list1

        if list2:
            tail.next = list2

        # ---------------------------------------------------------
        # STEP 5
        #
        # Return dummy.next
        #
        # Why not dummy?
        #
        # Because dummy is a fake node.
        #
        # dummy → 1 → 2 → 3
        #
        # We want:
        #
        # 1 → 2 → 3
        # ---------------------------------------------------------
        return dummy.next