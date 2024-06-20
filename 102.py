class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def bfs(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        
        q = deque([(root, 0)])
        levels = []

        while q:
            node, level = q.popleft()
            if len(levels) == level:
                levels.append([])
            levels[level].append(node.val)
            
            if node.left:
                q.append((node.left, level + 1))
            if node.right:
                q.append((node.right, level + 1))
        
        return levels
        
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        return self.bfs(root)
