"""
# Definition for a Node.
class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.parent = None
"""

class Solution:
    def lowestCommonAncestor(self, p: 'Node', q: 'Node') -> 'Node':
        pointer1 = p 
        pointer2 = q
        while pointer1 != pointer2:
            if pointer1 is None:
                pointer1 = q 
            else:
                pointer1 = pointer1.parent
            if pointer2 is None:
                pointer2 = p 
            else:
                pointer2 = pointer2.parent 
        return pointer1                    
