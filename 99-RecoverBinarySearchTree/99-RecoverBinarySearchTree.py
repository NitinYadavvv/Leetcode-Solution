# Last updated: 1/18/2026, 6:21:45 PM
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def recoverTree(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: None Do not return anything, modify root in-place instead.
        """
        inorder = []

        def helper(root):
            if not root:
                return 
            
            helper(root.left)
            inorder.append(root)
            helper(root.right)
        helper(root)
        index = 0
        first = None
        second = None
        for i in range(len(inorder)-1):
            if inorder[i].val > inorder[i+1].val:
                first = inorder[i]
                second = inorder[i+1]
                index = i
                break
        for j in range(index+1,len(inorder)-1):
            if inorder[j].val > inorder[j+1].val:
                second = inorder[j+1]
        first.val , second.val = second.val , first.val