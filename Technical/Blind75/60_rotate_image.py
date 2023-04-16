'''
https://leetcode.com/problems/rotate-image/
'''
class Solution:
  def rotate(self, matrix: List[List[int]]) -> None:
      n = len(matrix)
        
      i = 0
      j = n - 1      
      while i < j:
          for row in range(0, n):
              temp = matrix[row][i]
              matrix[row][i] = matrix[row][j]
              matrix[row][j] = temp     
          i += 1
          j -= 1
        
      for i in range(0, n):
          for j in range(0, n - i - 1):
              temp = matrix[i][j]
              matrix[i][j] = matrix[n - j - 1][n - i - 1]
              matrix[n - j - 1][n - i - 1] = temp