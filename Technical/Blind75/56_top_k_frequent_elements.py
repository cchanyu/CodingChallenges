'''
https://leetcode.com/problems/top-k-frequent-elements/
'''
class Solution:
  def topKFrequent(self, nums: List[int], k: int) -> List[int]:
      lookup = {}
      ans = []
      freq = [[] for i in range(len(nums) + 1)]
        
      for x in nums:
          lookup[x] = lookup.get(x, 0) + 1
            
      for key, value in lookup.items():
          freq[value].append(key)
            
      for i in range(len(freq) - 1, 0, -1):
          for n in freq[i]:
              ans.append(n)
              if len(ans) == k:
                  return ans