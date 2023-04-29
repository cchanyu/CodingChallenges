'''
https://leetcode.com/problems/meeting-rooms-ii/
'''
class Solution:
  def minMeetingRooms(self, intervals: List[List[int]]) -> int:
      start = sorted([i[0] for i in intervals])
      end = sorted([i[1] for i in intervals])
        
      ans, cnt = 0, 0
      s, e = 0, 0
        
      while s < len(intervals):
          if start[s] < end[e]:
              s += 1
              cnt += 1
                
          else:
              e += 1
              cnt -= 1
                
          ans = max(ans, cnt)
            
      return ans