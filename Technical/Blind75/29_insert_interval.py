'''
https://leetcode.com/problems/insert-interval/
'''
class Solution:
  def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
      arr = []
      ans = []
      flag = False

      for x in intervals:
          arr.append(x)
        
      for i in range(len(arr)):
          if arr[i][0] >= newInterval[0]:
              arr.insert(i, newInterval)
              flag = True
              break
                
      if not flag:
          arr.append(newInterval)
            
      for x in arr:
          if len(ans) == 0 or ans[-1][1] < x[0]:
              ans.append(x)
          else:
              ans[-1][1] = max(ans[-1][1], x[1])
                
      return ans