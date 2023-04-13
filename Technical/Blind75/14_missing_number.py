'''
https://leetcode.com/problems/missing-number/
'''
class Solution:
  def missingNumber(self, nums: List[int]) -> int:
      n = len(nums)       
      k = 0
        
      for i in range(1, n + 1):
          k ^= i
          k ^= nums[i - 1]

      return k