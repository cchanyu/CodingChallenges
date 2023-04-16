'''
https://leetcode.com/problems/number-of-connected-components-in-an-undirected-graph/
'''
class Solution:
  def countComponents(self, n: int, edges: List[List[int]]) -> int:
      ans = 0
      vis = [False] * n
      g = [0] * n
        
      for i in range(n):
          g[i] = []
            
      for e in edges:
          g[e[0]].append(e[1])
          g[e[1]].append(e[0])
            
      def dfs(u):
          vis[u] = True
          for v in g[u]:
              if not vis[v]:
                  dfs(v)
                    
      for i in range(n):
          if not vis[i]:
              dfs(i)
              ans += 1
                
      return ans