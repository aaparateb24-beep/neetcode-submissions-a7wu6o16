class Solution:

    def buildTree(self, preorder, inorder):

        # Maps every value to its index
        # in inorder.
        #
        # This avoids searching every time.
        inorderMap = {}

        for i in range(len(inorder)):
            inorderMap[inorder[i]] = i

        # Points to current root
        # in preorder traversal.
        self.preIndex = 0

        def build(left, right):

            # No nodes left.
            if left > right:
                return None

            # First unused preorder element
            # is always the root.
            rootValue = preorder[self.preIndex]

            self.preIndex += 1

            # Create root node.
            root = TreeNode(rootValue)

            # Find root position
            # in inorder.
            mid = inorderMap[rootValue]

            # Everything left of mid
            # belongs to left subtree.
            root.left = build(left, mid - 1)

            # Everything right of mid
            # belongs to right subtree.
            root.right = build(mid + 1, right)

            return root

        return build(0, len(inorder) - 1)