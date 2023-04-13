'''
https://leetcode.com/problems/jump-game/
'''
class Solution:
  def canJump(self, nums: List[int]) -> bool:
      n = len(nums)
      step = nums[0]
        
      for i in range(n):
          if i + nums[i] >= n - 1:
              return True
            
          if step <= 0:
              return False
            
          step = max(step - 1, nums[i + 1])
            
      return False