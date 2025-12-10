# Last updated: 12/10/2025, 8:21:57 AM
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from collections import deque
class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        l = []
        def do(root):
            if root is None:
                l.append('#')
                return
            l.append(str(root.val))
            do(root.left)
            do(root.right)
        do(root)

        return ','.join(l)

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        l = data.split(',')
        l = l[::-1]
        def helper(l):
            val = l.pop()
            print(val)
            if val == '#':
                return None
            
            node = TreeNode(val)
            node.left = helper(l)
            node.right = helper(l)

            return node
        
        return helper(l)
        

        

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))