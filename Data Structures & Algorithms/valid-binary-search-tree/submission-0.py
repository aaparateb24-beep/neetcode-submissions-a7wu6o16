class Solution:
    def isValidBST(self, root):

        def dfs(node, low, high):

            # Base case
            if not node:
                return True

            # Invalid value
            if node.val <= low or node.val >= high:
                return False

            # These lines should NOT be inside the if block
            left = dfs(node.left, low, node.val)
            right = dfs(node.right, node.val, high)

            return left and right

        return dfs(root, float("-inf"), float("inf"))