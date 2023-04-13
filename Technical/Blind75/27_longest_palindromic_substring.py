'''
https://leetcode.com/problems/longest-palindromic-substring/
'''
class Solution:
  def longestPalindrome(self, s: str) -> str:
      n = len(s)
      max = 0
      L, R = 0, 0
        
      dp = [[ 0 for j in range(n + 1) ] for i in range(n + 1)]
        
      for i in range(n):
          for j in range(i, -1, -1):
                
              if s[j] == s[i] and (i - j <= 2 or dp[j + 1][i - 1]):
                  dp[j][i] = True
                    
                  if (i - j + 1) > max:
                      max = i - j + 1
                      L = j
                      R = i
                        
      return s[L:R + 1]