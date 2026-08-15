class Solution:
    def postorder(self, root):

        result = []
        def dfs(node):
            if node is None:
                return 
            # First, recursively visit EVERY child.
            #
            # We don't add 'node' yet because this is POSTORDER.
            # Children must come before the current node.
            for child in node.children:
                dfs(child)   
            result.append(node.val)
        dfs(root) 
        return result       