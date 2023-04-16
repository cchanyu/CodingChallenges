'''
https://leetcode.com/problems/set-matrix-zeroes/
'''
class Solution:
  def setZeroes(self, matrix: List[List[int]]) -> None:
      if not matrix:
          return []
        
      m = len(matrix)
      n = len(matrix[0])
        
      rowflag = [1] * m
      colflag = [1] * n
        
      for row in range(m):
          for col in range(n):
              if matrix[row][col] == 0:
                  rowflag[row] = 0
                  colflag[col] = 0
                    
      for row in range(m):
          for col in range(n):
              if rowflag[row] == 0 or colflag[col] == 0:
                  matrix[row][col] = 0