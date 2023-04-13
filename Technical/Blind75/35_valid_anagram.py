'''
https://leetcode.com/problems/valid-anagram/
'''
class Solution:
  def isAnagram(self, s: str, t: str) -> bool:
      tracker = defaultdict(int)

      for c in s:
          tracker[c] += 1

      for c in t:
          tracker[c] -= 1
            
      for x in tracker.values():
          if x != 0:
              return False
      return True