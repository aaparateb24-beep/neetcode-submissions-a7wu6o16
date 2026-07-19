# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        dummy = ListNode(0)
        dummy.next = head
        prev = dummy 
        curr = head
        # Move to left position
        for _ in range(left - 1):
            prev = curr 
            curr = curr.next 
        # Save nodes    
        connection = prev
        tail = curr
        
        #reverse
        prev = None
        for _ in range(right - left + 1):
            next = curr.next
            curr.next = prev
            prev = curr
            curr = next 
        # Reconnect
        connection.next = prev
        tail.next = curr
        return dummy.next 
