class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def validate(root, left, right):
            if not root:
                return True
            
            if not ((root.val > left) and (root.val < right)):
                return False
            
            return validate(root.left, left, root.val) and validate(root.right, root.val, right)
        
        return validate(root, float('-inf'), float('inf'))
