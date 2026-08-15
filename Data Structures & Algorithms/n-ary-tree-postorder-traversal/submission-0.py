class Solution:
    def postorder(self, root):

        # This will contain our final traversal.
        result = []

        def dfs(node):

            # Base case:
            # If there is no node, there is nothing to visit.
            if node is None:
                return

            # First, recursively visit EVERY child.
            #
            # We don't add 'node' yet because this is POSTORDER.
            # Children must come before the current node.
            for child in node.children:
                dfs(child)

            # Only AFTER all children have been completely processed
            # do we add the current node.
            result.append(node.val)

        # Start recursion from the root.
        dfs(root)

        return result  