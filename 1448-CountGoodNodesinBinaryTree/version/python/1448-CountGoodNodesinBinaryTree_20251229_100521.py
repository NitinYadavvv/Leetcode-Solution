# Last updated: 12/29/2025, 10:05:21 AM
# need to do it again
1class Solution(object):
2    def goodNodes(self, root):
3        def dfs(node, max_so_far):
4            if not node:
5                return 0
6            
7            good = 1 if node.val >= max_so_far else 0
8            max_so_far = max(max_so_far, node.val)
9            
10            return good + dfs(node.left, max_so_far) + dfs(node.right, max_so_far)
11        
12        return dfs(root, root.val)
13