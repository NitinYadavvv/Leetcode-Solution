# Last updated: 1/12/2026, 11:27:00 PM
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution(object):
    def buildTree(self, inorder, postorder):
        """
        :type inorder: List[int]
        :type postorder: List[int]
        :rtype: Optional[TreeNode]
        """
        if not inorder or not postorder:
            return None
        
        # value -> index mapping for inorder
        index_map = {val: i for i, val in enumerate(inorder)}
        
        def helper(in_left, in_right):
            if in_left > in_right:
                return None
            
            # last element in postorder is the root
            root_val = postorder.pop()
            root = TreeNode(root_val)
            
            # split inorder list
            index = index_map[root_val]
            
            # IMPORTANT: build right subtree first
            root.right = helper(index + 1, in_right)
            root.left = helper(in_left, index - 1)
            
            return root
        
        return helper(0, len(inorder) - 1)
