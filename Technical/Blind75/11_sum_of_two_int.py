'''
https://leetcode.com/problems/sum-of-two-integers/
'''
class Solution:
  def getSum(self, a: int, b: int) -> int:
      MASK = 0xFFF
      INT_MAX = 0x7FF
        
      sumVal = (a ^ b) & MASK      
      carry = ((a & b) << 1) & MASK
        
      while carry:
          return self.getSum(sumVal, carry)
        
      return sumVal if sumVal <= INT_MAX else ~ (sumVal ^ MASK)