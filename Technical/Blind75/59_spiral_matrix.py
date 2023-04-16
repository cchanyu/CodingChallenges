'''
https://leetcode.com/problems/spiral-matrix/
'''
class Solution:
  def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
      ans = []
      m = len(matrix)
      n = len(matrix[0])
        
      rBegin, rEnd = 0, m - 1
      cBegin, cEnd = 0, n - 1
        
      while True:
          for i in range(cBegin, cEnd + 1):
              ans.append(matrix[rBegin][i])
          rBegin += 1
          if rBegin > rEnd:
              break
                
          for i in range(rBegin, rEnd + 1):
              ans.append(matrix[i][cEnd])
          cEnd -= 1
          if cEnd < cBegin:
              break
                
          for i in range(cEnd, cBegin - 1, -1):
              ans.append(matrix[rEnd][i])
          rEnd -= 1
          if rEnd < rBegin:
              break
                
          for i in range(rEnd, rBegin - 1, -1):
              ans.append(matrix[i][cBegin])
          cBegin += 1
          if cBegin > cEnd:
              break
                
      return ans