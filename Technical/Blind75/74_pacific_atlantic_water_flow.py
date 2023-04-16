'''
https://leetcode.com/problems/pacific-atlantic-water-flow
'''
class Solution:
  def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
      directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
      m = len(heights)
      n = len(heights[0])
      ans = []
        
      g1 = [[0 for j in range(n + 1)] for i in range(m + 1)]
      g2 = [[0 for j in range(n + 1)] for i in range(m + 1)]
        
      def dfs(h, x, y, g):
          g[x][y] = 1
          for d in directions:
              nx = x + d[0]
              ny = y + d[1]
                
              if nx >= 0 and ny >= 0 and nx < len(h) and ny < len(h[0]) and h[nx][ny] >= h[x][y] and g[nx][ny] != 1:
                  dfs(h, nx, ny, g)
            
      for i in range(m):
          for j in range(n):
              if (i == 0 or j == 0):
                  dfs(heights, i, j, g1)
                
              if (i == m - 1 or j == n - 1):
                  dfs(heights, i, j, g2)
                    
      for i in range(m):
          for j in range(n):
              if g1[i][j] == 1 and g2[i][j] == 1:
                  ans.append((i, j))
                    
      return ans