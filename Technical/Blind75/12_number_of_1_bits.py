'''
https://leetcode.com/problems/number-of-1-bits/
'''
class Solution:
  def hammingWeight(self, n: int) -> int:
      count = 0
      while n:
          if n & 1 > 0:
              count += 1
          n = n >> 1  
      
      return count