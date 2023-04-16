'''
https://leetcode.com/problems/minimum-window-substring/
'''
class Solution:
  def minWindow(self, s: str, t: str) -> str:
      ans = ''
      cnt = 0
      mnLen = float('inf') 
      cur = {}
      tDict = {}
        
      for c in t:
          tDict[c] = tDict.get(c, 0) + 1
            
      i = 0  
      for j in range(len(s)):
            
          if s[j] in tDict:
              cur[s[j]] = cur.get(s[j], 0) + 1
                
              if cur[s[j]] == tDict[s[j]]:
                  cnt += 1
                    
          while cnt == len(tDict):
                
              if j - i + 1 < mnLen:
                  ans = s[i : j + 1]
                  mnLen = j - i + 1
                    
              if s[i] in tDict:
                    
                  cur[s[i]] = cur.get(s[i], 0) - 1
                
                  if cur[s[i]] == tDict[s[i]] - 1:
                      cnt -= 1
              i += 1
                
      return ans