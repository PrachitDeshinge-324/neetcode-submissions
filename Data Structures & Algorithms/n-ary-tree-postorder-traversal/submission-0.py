"""
# Definition for a Node.
class Node:
    def __init__(self, val: Optional[int] = None, children: Optional[List['Node']] = None):
        self.val = val
        self.children = children
"""

class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        ans = []
        def post(node):
            if node is None:
                return
            for c in node.children:
                post(c)
            ans.append(node.val)
        post(root)
        return ans