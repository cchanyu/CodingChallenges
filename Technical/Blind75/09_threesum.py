'''
https://leetcode.com/problems/3sum/
'''
class Solution:
  def threeSum(self, nums: List[int]) -> List[List[int]]:
      ans = []
      nums = sorted(nums)
      n = len(nums)

      for i in range(0, n - 2):
          j = i + 1
          k = n - 1
          
          if nums[i] > 0:
              break
              
          if i > 0 and nums[i] == nums[i - 1]:
              continue
              
          while j < k:
              
              total = nums[i] + nums[j] + nums[k]

              if total > 0:
                  k -= 1
                  
              elif total < 0:
                  j += 1
                  
              else:
                  ans.append([nums[i], nums[j], nums[k]])
                  j += 1
                  k -= 1
                  
                  while j < k and nums[j] == nums[j - 1]:
                      j += 1
                      
                  while j < k and nums[k] == nums[k + 1]:
                      k -= 1
                      
      return ans