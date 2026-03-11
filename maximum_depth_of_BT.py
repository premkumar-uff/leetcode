class Solution(object):
    def maxDepth(self, root):
        if root is None:
            return 0       
        if root.left is None:
            return 1 + self.maxDepth(root.right)       
        if root.right is None:
            return 1 + self.maxDepth(root.left)       
        return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))
        
