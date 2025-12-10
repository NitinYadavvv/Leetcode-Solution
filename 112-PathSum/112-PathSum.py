# Last updated: 12/10/2025, 8:22:58 AM
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def hasPathSum(self, root, targetSum):
        """
        :type root: Optional[TreeNode]
        :type targetSum: int
        :rtype: bool
        """
        if not root:
            return False
        
        sum = targetSum
        ans = False
        def hel(root,sum):
            if not root:
                return False
            sum = sum-root.val
            if sum == 0 and not root.left and not root.right:
                return True
            
            return hel(root.left,sum) or hel(root.right,sum)


        return hel(root,sum)

            

            
            

        
        