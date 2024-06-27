from collections import defaultdict

class Solution:
    def dfs(self, graph, visited, rates, start):
        visited[start] = 1
        for i in graph[start]:
            if visited[i[0]] == 0:
                rates[i[0]] = abs(rates[start]) * i[1]
                self.dfs(graph, visited, rates, i[0])
        return rates

    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        graph = defaultdict(list)
        
        for i in range(len(equations)):
            a = equations[i][0]
            b = equations[i][1]
            graph[a].append([b, values[i]])
            graph[b].append([a, 1 / values[i]])
              
        ans = []
        for start, end in queries:
            if start not in graph or end not in graph:
                ans.append(-1.0)
                continue
            visited = defaultdict(int)
            rates = defaultdict(lambda: -1)
            rates[start] = 1.0
            self.dfs(graph, visited, rates, start)
            if rates[end] == -1.0:
                ans.append(-1.0)
            else:
                ans.append(rates[end])
        return ans
            
        
        
