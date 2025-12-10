# Last updated: 12/10/2025, 8:23:00 AM
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def minDepth(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        if root is None:
            return 0
        level = 0
        q = deque([root])
        while q:
            l = len(q)
            level+=1
            while l:
                node = q.popleft()
                if not node.left and not node.right:
                    return level
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
                
                l-=1
        return level

        