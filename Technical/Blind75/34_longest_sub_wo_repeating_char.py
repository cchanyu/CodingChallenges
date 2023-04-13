'''
https://leetcode.com/problems/longest-substring-without-repeating-characters/
'''
class Solution:
  def lengthOfLongestSubstring(self, s: str) -> int:
      unique = set()
      l = 0
      ans = 0
        
      for r in range(len(s)):
          while s[r] in unique:
              unique.remove(s[l])
              l += 1
                    
          unique.add(s[r])
            
          ans = max(ans, r - l + 1)
            
      return ans