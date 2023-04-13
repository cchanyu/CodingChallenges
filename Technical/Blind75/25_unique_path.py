'''
https://leetcode.com/problems/unique-paths/
'''
class Solution:
  def uniquePaths(self, m: int, n: int) -> int:
      dp = [[ 0 for j in range(n + 1) ] for i in range(m + 1)]
        
      for i in range(m):
          for j in range(n):
              if i == 0 or j == 0:
                  dp[i][j] = 1
              else:
                  dp[i][j] += dp[i - 1][j] + dp[i][j - 1]
                    
      return dp[m - 1][n - 1]

class Solution:     
  def uniquePaths(self, m: int, n: int) -> int:
      d = {}

      def helper(i , j):
          if i > m or j > n:
              return 0
            
          if i == m - 1 and j == n - 1:
              return 1
            
          if (i, j) in d:
              return d[(i, j)]
            
          d[(i, j)] = helper(i + 1, j) + helper(i, j + 1)
          return d[(i, j)]
        
      return helper(0, 0)