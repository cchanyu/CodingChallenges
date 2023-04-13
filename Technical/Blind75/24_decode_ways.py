'''
https://leetcode.com/problems/decode-ways/
'''
class Solution:
  def numDecodings(self, s: str) -> int:
      n = len(s)
        
      dp = [0] * (n + 1)
      dp[0] = 1
        
      for i in range(0, n):
          if s[i] > '0':
              dp[i + 1] = dp[i]
                
          if (i > 0 and (s[i - 1] == '1' or (s[i - 1] == '2' and s[i] <= '6'))):
              dp[i + 1] += dp[i - 1]
                     
      return dp[n]