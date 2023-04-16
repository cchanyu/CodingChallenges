'''
https://leetcode.com/problems/word-search/
'''
class Solution:
  def exist(self, board: List[List[str]], word: str) -> bool:
      directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
      n = len(board)
      m = len(board[0])
      used = [[False for j in range(m)] for i in range(n)]
        
      def dfs(board, word, x, y, idx):
          if board[x][y] != word[idx]:
              return False
            
          if idx == len(word) - 1:
              return True
            
          used[x][y] = True
            
          for d in directions:
              nx = x + d[0]
              ny = y + d[1]
                
              if nx >= 0 and ny >= 0 and nx < len(board) and ny < len(board[0]) and not used[nx][ny]:
                  if dfs(board, word, nx, ny, idx + 1):
                      return True
                    
          used[x][y] = False
          return False
        
      for i in range(n):
          for j in range(m):
              if dfs(board, word, i, j, 0):
                  return True
                
      return False