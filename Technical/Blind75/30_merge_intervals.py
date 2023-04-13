'''
https://leetcode.com/problems/merge-intervals/
'''
class Solution:
  def merge(self, intervals: List[List[int]]) -> List[List[int]]:
      ans = []
      intervals.sort()
        
      for x in intervals:
          if len(ans) == 0 or ans[-1][1] < x[0]:
              ans.append(x)
            
          else:
              ans[-1][1] = max(ans[-1][1], x[1])
                
      return ans