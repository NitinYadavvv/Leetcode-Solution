# Last updated: 2/9/2026, 7:11:00 AM
# first take inorder then construct the tree using recursion
1# Definition for a binary tree node.
2# class TreeNode:
3#     def __init__(self, val=0, left=None, right=None):
4#         self.val = val
5#         self.left = left
6#         self.right = right
7class Solution:
8    def balanceBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
9        self.inodr = []
10        def inorder(root):
11            if root is None:
12                return 
13            
14            inorder(root.left)
15            self.inodr.append(root.val)
16            inorder(root.right)
17        
18        def make(arr):
19            if len(arr) == 0:
20                return None
21            if len(arr) == 1:
22                return TreeNode(arr[0])
23            
24            mid = len(arr)//2
25            Node = TreeNode(arr[mid])
26            Node.left = make(arr[0:mid])
27            Node.right = make(arr[mid+1:])
28            return Node
29        inorder(root)
30        return make(self.inodr)
31        