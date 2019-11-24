class Solution(object):
    def zigzagLevelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if root == None:
            return []
        
        result = []
        level = [root]
        
        # easier to use this instead of true/false
        direction = 1

        while level:
            result.append([n.val for n in level][::direction])
            direction *= -1
            level = [kid for node in level for kid in (node.left, node.right) if kid]
            
        return result