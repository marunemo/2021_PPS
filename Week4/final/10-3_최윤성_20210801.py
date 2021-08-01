class Solution(object):
    def hasPathSum(self, root, targetSum):
        if not root:
            return False
        
        queue = [root]
        while queue:
            node = queue.pop(0)
            if node.left or node.right:
                if node.left:
                    node.left.val += node.val
                    queue.append(node.left)
                if node.right:
                    node.right.val += node.val
                    queue.append(node.right)
            elif node.val == targetSum:
                return True
        return False