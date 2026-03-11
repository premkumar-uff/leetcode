class Solution(object):
    def deleteNode(self, root, key):
        if not root:
            return None        
        if root.val == key:
            return self.process(root)        
        dummy = root        
        while root:
            if key < root.val:
                if root.left and root.left.val == key:
                    root.left = self.process(root.left)
                    break
                else:
                    root = root.left
            else:
                if root.right and root.right.val == key:
                    root.right = self.process(root.right)
                    break
                else:
                    root = root.right       
        return dummy
    def process(self, root):
        if not root.left:
            return root.right
        if not root.right:
            return root.left       
        rightside = root.right
        leftside = self.findlast(root.left)
        leftside.right = rightside       
        return root.left
    def findlast(self, root):
        while root.right:
            root = root.right
        return root
