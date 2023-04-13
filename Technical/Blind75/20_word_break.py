'''
https://leetcode.com/problems/word-break/
'''
class Solution:
  def wordBreak(self, s: str, wordDict: List[str]) -> bool:
      w = set(wordDict)     
      n = len(s)
        
      dp = [False] * (n + 1)
      dp[0] = True
        
      for i in range(1, n + 1):
          for j in range(0, i):
                
              if dp[j] and s[j:i] in w:
                  dp[i] = True
                  break
                    
      return dp[n]