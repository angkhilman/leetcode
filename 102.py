from collections import deque

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def bfs(self, root):
        q = deque()
        d = []
        q.append((root, 0))

        while q:
            current = q.popleft()
            if current[0]:
                if d:
                    if len(d) - 1 == current[1]:
                        d[-1].append(current[0].val)
                    else:
                        d.append([current[0].val])
                else:
                    d.append([current[0].val])
                q.append((current[0].left, current[1] + 1))
                q.append((current[0].right, current[1] + 1))
        return d
        
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        return self.bfs(root)
