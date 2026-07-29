# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        slow = head 
        fast = head 
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        # Step 2: Reverse the second half
        prev = None
        curr = slow 
        while curr:
            nxt = curr.next 
            curr.next = prev
            prev = curr 
            curr = nxt
        # Step 2: Reverse the second half
        second = prev
        first = head 
        ans = 0 
        while second:
            ans = max(ans, first.val + second.val)
            first = first.next 
            second = second.next 
        return ans             