class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        q = collections.deque()
        res = []

        if root:
            q.append(root)
        
        while q:
            rightSide = None

            for i in range(len(q)):
                node = q.popleft()
                if node:
                    q.append(node.left)
                    q.append(node.right)
                    rightSide = node.val
            if rightSide:
                res.append(rightSide)

            
        return res
