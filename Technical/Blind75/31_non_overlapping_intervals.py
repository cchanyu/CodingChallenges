'''
https://leetcode.com/problems/non-overlapping-intervals/
'''
class Solution:
  def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
      r = float('-inf')
      ans = 0
        
      intervals.sort()
        
      for x in intervals:
          if r > x[0]:
              r = min(r, x[1])
              ans += 1
                
          else:
              r = x[1]
                
      return ans