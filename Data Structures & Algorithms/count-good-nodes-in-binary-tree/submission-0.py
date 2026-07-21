# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        good = 0 
        def dfs(node, max_so_far):
            nonlocal good
            if not node :
                return  None
            # If current node is greater than or
            # equal to every value seen so far,
            # then it is a good node.
            if node.val >= max_so_far:
                good += 1
             # Update the maximum value seen on the
            # path before visiting children.
            # ---------------------------------------
            new_max = max(max_so_far, node.val)
            # ---------------------------------------
            # Visit left subtree.
            #
            # Pass the updated maximum.
            # --------------------------------------
            dfs(node.left, new_max)
            dfs(node.right, new_max)
         # Initially no value has been seen.
        #
        # So start with negative infinity.
        # ---------------------------------------
        dfs(root, float('-inf'))

        return good            