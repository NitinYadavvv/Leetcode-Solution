# Last updated: 12/10/2025, 8:23:08 AM
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: Optional[TreeNode]
        """
        if len(inorder) == 0 or len(preorder) == 0:
            return None
        
        root = TreeNode(preorder[0])
        index = 0
        for i in range(len(inorder)):
            if root.val == inorder[i]:
                index = i
                break
        
        root.left = self.buildTree(preorder[1:index+1],inorder[0:index])
        root.right = self.buildTree(preorder[index+1:len(preorder)],inorder[index+1:len(inorder)])

        return root

        