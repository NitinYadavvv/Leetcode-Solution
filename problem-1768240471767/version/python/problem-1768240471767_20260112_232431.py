# Last updated: 1/12/2026, 11:24:31 PM
# use inorder then traverse inorder where you find you first deflect that will be your first deflect then resume traversing if you find your second deflect that is your second swap both here is your answer but if you wont find the the any deflect after resume its mean you second is the next element after first
1# Definition for a binary tree node.
2# class TreeNode(object):
3#     def __init__(self, val=0, left=None, right=None):
4#         self.val = val
5#         self.left = left
6#         self.right = right
7class Solution(object):
8    def recoverTree(self, root):
9        """
10        :type root: Optional[TreeNode]
11        :rtype: None Do not return anything, modify root in-place instead.
12        """
13        inorder = []
14
15        def helper(root):
16            if not root:
17                return 
18            
19            helper(root.left)
20            inorder.append(root)
21            helper(root.right)
22        helper(root)
23        index = 0
24        first = None
25        second = None
26        for i in range(len(inorder)-1):
27            if inorder[i].val > inorder[i+1].val:
28                first = inorder[i]
29                second = inorder[i+1]
30                index = i
31                break
32        for j in range(index+1,len(inorder)-1):
33            if inorder[j].val > inorder[j+1].val:
34                second = inorder[j+1]
35        first.val , second.val = second.val , first.val