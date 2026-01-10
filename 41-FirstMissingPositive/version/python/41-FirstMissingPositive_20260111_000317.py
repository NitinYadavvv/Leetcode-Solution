# Last updated: 1/11/2026, 12:03:17 AM
1# Definition for a binary tree node.
2# class TreeNode(object):
3#     def __init__(self, val=0, left=None, right=None):
4#         self.val = val
5#         self.left = left
6#         self.right = right
7
8class Solution(object):
9    def buildTree(self, inorder, postorder):
10        """
11        :type inorder: List[int]
12        :type postorder: List[int]
13        :rtype: Optional[TreeNode]
14        """
15        if not inorder or not postorder:
16            return None
17        
18        # value -> index mapping for inorder
19        index_map = {val: i for i, val in enumerate(inorder)}
20        
21        def helper(in_left, in_right):
22            if in_left > in_right:
23                return None
24            
25            # last element in postorder is the root
26            root_val = postorder.pop()
27            root = TreeNode(root_val)
28            
29            # split inorder list
30            index = index_map[root_val]
31            
32            # IMPORTANT: build right subtree first
33            root.right = helper(index + 1, in_right)
34            root.left = helper(in_left, index - 1)
35            
36            return root
37        
38        return helper(0, len(inorder) - 1)
39