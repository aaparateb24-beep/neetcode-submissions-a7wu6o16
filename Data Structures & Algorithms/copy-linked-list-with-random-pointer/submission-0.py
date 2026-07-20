"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None
        copy = {}   #hashmap 
        curr = head 
         # PASS 1
        #
        # Create a NEW node for every original node.
        #
        # IMPORTANT:
        # We are NOT connecting anything yet.
        #
        # Original:
        #
        # A -> B -> C
        #
        # After Pass 1:
        #
        # A'
        #
        # B'
        #
        # C'
        #
        # Dictionary:
        #
        # A -> A'
        # B -> B'
        # C -> C'
        while curr:
            copy[curr] = Node(curr.val)
            curr = curr.next 
        # First pass finished.
        #
        # curr has reached None.
        #
        # We need to start from beginning again.
        # -------------------------------------------------
        curr = head
    
        while curr:
         # CONNECT NEXT POINTER
            #
            # Suppose:
            #
            # curr = A
            #
            # Original:
            #
            # A -> B
            #
            # We want:
            #
            # A' -> B'
            #
            #
            # Step by step:
            #
            # copy[curr]
            #
            # becomes
            #
            # copy[A]
            #
            # which is
            #
            # A'
            #
            #
            # curr.next
            #
            # becomes
            #
            # B
            #
            #
            # copy.get(B)
            #
            # becomes
            #
            # B'
            #
            #
            # Therefore:
            #
            # A'.next = B'
            #
            #
            # Why use get()?
            #
            # If curr.next is None,
            #
            # copy.get(None)
            #
            # automatically returns None.    
            copy[curr].next = copy.get(curr.next)
            copy[curr].random = copy.get(curr.random)   
            curr = curr.next 
         # head is original head.
        #
        # Example:
        #
        # head
        #  ↓
        # A
        #
        #
        # copy[head]
        #
        # becomes
        #
        # copy[A]
        #
        # which is
        #
        # A'
        #
        # Return copied head.    
        return copy[head]     