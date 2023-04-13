'''
https://leetcode.com/problems/meeting-rooms/
'''
class Solution:
  def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
      if len(intervals) <= 1:
          return True
        
      intervals.sort()
        
      r = -1
        
      for x in intervals:
          if x[0] < r:
              return False
          r = x[1]
            
      return True