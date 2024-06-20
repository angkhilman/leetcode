# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorder(self, root):
        if root:
            left_val = self.postorder(root.left)
            right_val = self.postorder(root.right)
            return max(left_val, right_val) + 1
        else:
            return 0

    def maxDepth(self, root: Optional[TreeNode]) -> int:
        return self.postorder(root)

        
