'''
https://leetcode.com/problems/longest-repeating-character-replacement/
'''
class Solution:
  def characterReplacement(self, s: str, k: int) -> int:
      cnt = [0] * 26
      ans, maxNm = 0, 0
        
      l = 0
      for i in range(len(s)):
          cnt[ord(s[i]) - ord('A')] += 1
          maxNm = max(maxNm, cnt[ord(s[i]) - ord('A')])
            
          if (i - l + 1 - maxNm) > k:
              cnt[ord(s[l]) - ord('A')] -= 1
              l += 1
                
          ans = max(ans, i - l + 1)
            
      return ans