'''
https://leetcode.com/problems/house-robber-ii/
'''
class Solution:
  def rob(self, nums: List[int]) -> int:
      n = len(nums)
        
      if n == 1:
          return nums[0]
        
      n -= 1
        
      dp1 = [0] * (n + 1)
      dp2 = [0] * (n + 1)
        
      dp1[1] = nums[0]
      dp2[1] = nums[1]
        
      for i in range(2, n + 1):
          dp1[i] = max(dp1[i - 1], nums[i - 1] + dp1[i - 2])
          dp2[i] = max(dp2[i - 1], nums[i] + dp2[i - 2])
            
      return max(dp1[n], dp2[n])