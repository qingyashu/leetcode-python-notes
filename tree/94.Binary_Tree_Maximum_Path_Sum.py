"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""

class Solution:
    res = None
    
    """
    @param root: The root of binary tree.
    @return: An integer
    """
    def maxPathSum(self, root):
        self.res = None
        self.dfs(root)
        return self.res
        
    def dfs(self, root):
        if root is None:
            return 0
        left = self.dfs(root.left)
        right = self.dfs(root.right)
        self.res = max(self.res, root.val, left + right + root.val, left + root.val, right + root.val)
        return max(left + root.val, right + root.val)
