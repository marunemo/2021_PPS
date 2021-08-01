class Solution(object):
    def hasPathSum(self, root, targetSum):
        if not root.left and not root.right:
            return root.val == targetSum
        
        if root.left:
            root.left.val += root.val
            if Solution.hasPathSum(root.left, targetSum):
                return True
        if root.right:
            root.right.val += root.val
            if Solution.hasPathSum(root.right, targetSum):
                return True
        return False