from collections import defaultdict
class Solution:
    def dfs(self, visited, stack, g, v):
        if stack[v] == 1:
            return True
        if visited[v] == 1:
            return False
        visited[v] = 1
        stack[v] = 1
        for i in g[v]:
            if self.dfs(visited, stack, g, i):
                return True
        stack[v] = 0
        return False

    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        g = defaultdict(list)
        for f, s in prerequisites:
            g[f].append(s)
        visited = [0 for i in range(numCourses)]
        stack = [0 for i in range(numCourses)]
        for i in range(numCourses):
            if visited[i] == 0:
                if self.dfs(visited, stack, g, i):
                    return False
        return True
