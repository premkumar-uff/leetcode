from collections import deque
class Solution(object):
    def levelOrder(self, root):
        if not root:
            return []
        result=[]
        queue=deque()
        queue.append(root)
        while queue:
            l=[]
            size=len(queue)
            for i in range(size):
                a=queue.popleft()
                l.append(a.val)
                if a.left:
                    queue.append(a.left)
                if a.right:
                    queue.append(a.right)
            result.append(l)
        return result
