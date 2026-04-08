from collections import deque
from typing import List, Optional

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []

        result = [] #final ans will be stored here 
        queue = deque([root])

        while queue:
            level = [] #stored current level only 
            size = len(queue)

            for _ in range(size):
                node = queue.popleft() #remove node from front and add its value to level 
                level.append(node.val)

                if node.left:
                    queue.append(node.left) #if left child exists push to queue 
                if node.right:
                    queue.append(node.right) # same for right

            result.append(level)

        return result