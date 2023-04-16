'''
https://leetcode.com/problems/graph-valid-tree/
'''
class Solution:
  def validTree(self, n: int, edges: List[List[int]]) -> bool:
      if len(edges) == 0:
          return n == 1
        
      if n - len(edges) >= 2:
          return False
        
      d = [0] * n
        
      for p in edges:
          d[p[0]] += 1
          d[p[1]] += 1
            
      q = deque()
      for i in range(n):
          if d[i] == 1:
              q.append(i)
                
      g = [0] * n
      for i in range(n):
          g[i] = []
        
      for p in edges:
          g[p[0]].append(p[1])
          g[p[1]].append(p[0])
            
      while q:
          n -= 1
          u = q.popleft()
          for v in g[u]:
              d[v] -= 1
              if d[v] == 1:
                  q.append(v)
                    
      return n == 0