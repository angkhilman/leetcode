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
        visited = {}
        rates = {}
        for i in range(len(equations)):
            a = equations[i][0]
            b = equations[i][1]
            graph[a].append([b, values[i]])
            graph[b].append([a, 1 / values[i]])
              
        ans = []
        for q in queries:
            start = q[0]
            end = q[1]
            for i in range(len(equations)):
                a = equations[i][0]
                b = equations[i][1]
                rates[a] = -1
                rates[b] = -1
                visited[a] = 0
                visited[b] = 0
            self.dfs(graph, visited, rates, start)
            if start == end and end in rates:
                ans.append(1)
            elif end in rates and start != end:
                ans.append(float(f"{rates[end]:.5f}"))
            else:
                ans.append(-1.0)
        print(ans)
        return ans
            
        
        
