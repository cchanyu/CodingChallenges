'''
https://leetcode.com/problems/number-of-islands/
'''
class Solution:
  def numIslands(self, grid: List[List[str]]) -> int:
      directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
      ans = 0
      m = len(grid)
      n = len(grid[0])
        
      def dfs(grid, i, j):
          grid[i][j] = '0'
            
          for d in directions:
              ni = i + d[0]
              nj = j + d[1]
                
              if ni < 0 or nj < 0 or ni == len(grid) or nj == len(grid[0]) or grid[ni][nj] == '0':
                  continue
                
              dfs(grid, ni, nj)
                
      for i in range(m):
          for j in range(n):
              if grid[i][j] == '1':
                  dfs(grid, i, j)
                  ans += 1
                    
      return ans