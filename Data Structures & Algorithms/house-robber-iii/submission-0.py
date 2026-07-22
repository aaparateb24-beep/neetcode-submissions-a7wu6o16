class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:

        def dfs(node):

            # -------------------------------------
            # Base Case
            #
            # Empty tree contributes nothing.
            #
            # Return:
            #
            # (skip, rob)
            #
            # = (0,0)
            # -------------------------------------
            if not node:
                return (0, 0)

            # -------------------------------------
            # Solve left subtree.
            #
            # left[0] = money if left child is skipped
            #
            # left[1] = money if left child is robbed
            # -------------------------------------
            left = dfs(node.left)

            # Solve right subtree.
            right = dfs(node.right)

            # -------------------------------------
            # Case 1
            #
            # We DO NOT rob current node.
            #
            # Then every child is free to choose
            # whichever option gives more money.
            # -------------------------------------
            skip = max(left) + max(right)

            # -------------------------------------
            # Case 2
            #
            # We rob current node.
            #
            # Then children CANNOT be robbed.
            #
            # So we must take the "skip" value
            # from both children.
            # -------------------------------------
            rob = node.val + left[0] + right[0]

            # Return both possibilities to parent.
            return (skip, rob)

        # Root can either be robbed or skipped.
        return max(dfs(root))
            
        