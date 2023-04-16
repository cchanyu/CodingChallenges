'''
https://leetcode.com/problems/longest-consecutive-sequence/
'''
class Solution:
  def longestConsecutive(self, nums: List[int]) -> int:
      ans = 0
      unique = set(nums)

      for num in unique:
            
          if (num - 1) in unique:
              continue
          i = 1
          while num + i in unique:
              i += 1
          ans = max(ans, i)
            
      return ans