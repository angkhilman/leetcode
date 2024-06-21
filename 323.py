from collections import defaultdict

class Solution:
    def dfs(self, v, visited, g):
        visited[v] = 1
        for i in g[v]:
            if visited[i] == 0:
                self.dfs(i, visited, g)

    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        graph = defaultdict(list)
        for i in edges:
            graph[i[0]].append(i[1])
            graph[i[1]].append(i[0])

        for i in range(n):
            if i not in graph:
                graph[i] = []
        
        visited = [0] * n
        count = 0

        for i in graph:
            if visited[i] == 0:
                count += 1
                self.dfs(i, visited, graph)

        return count
        
