# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def removeLeafNodes(self, root: Optional[TreeNode], target: int) -> Optional[TreeNode]:
        if not root:
            return None
         # ------------------------------------------------
        # First process the LEFT subtree.
        #
        # If left subtree gets deleted,
        # root.left will automatically become None.
        # ------------------------------------------------
        root.left = self.removeLeafNodes(root.left, target )
        root.right = self.removeLeafNodes(root.right,target)
         # ------------------------------------------------
        # Now both children have already been processed.
        #
        # It is possible that deleting children has made
        # the current node become a leaf.
        if (root.left is None and root.right is None and root.val is target):
            return None
        return root       