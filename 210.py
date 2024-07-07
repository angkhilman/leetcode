from collections import defaultdict

class Solution:
    def __init__(self):
        self.is_cycle = False
    def dfs(self, visited, g, v, path):
        if self.is_cycle:
            return 
        visited[v] = 1
        for i in g[v]:
            if visited[i] == 0:
                self.dfs(visited, g, i, path)
            elif visited[i] == 1:
                print(i)
                self.is_cycle = True
        visited[v] = 2
        path.append(v)


    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        n = numCourses
        g = defaultdict(list)
        for a, b in prerequisites:
            g[a].append(b)
        visited = [0 for i in range(n)]
        path = []
        for i in range(n):
            if visited[i] == 0:
                self.dfs(visited, g, i, path)
        return path if not self.is_cycle else []

        
