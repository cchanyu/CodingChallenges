'''
https://leetcode.com/problems/palindromic-substrings/
'''
class Solution:
  def countSubstrings(self, s: str) -> int:
      n = len(s)
      ans = 0
        
      dp = [[ 0 for j in range(n) ] for i in range(n)]
        
      for i in range(n):
          for j in range(i, -1, -1):
                
              if s[j] == s[i] and (i - j <= 2 or dp[j + 1][i - 1]):
                  ans += 1
                  dp[j][i] = True
                        
      return ans