'''
https://leetcode.com/problems/valid-parentheses/
'''
class Solution:
  def isValid(self, s: str) -> bool:
      lookup = {")": "(", 
                "}": "{",
                "]": "["}
        
      stack = []
        
      for i in range(len(s)):
          if s[i] not in lookup:
              stack.append(s[i])
                
          else:
              if len(stack) == 0 or stack[-1] != lookup[s[i]]:
                  return False
              stack.pop()
   
      return len(stack) == 0