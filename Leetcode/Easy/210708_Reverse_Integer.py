'''
Given a signed 32-bit integer x, return x with its digits reversed. If reversing x causes the value to go outside the signed 32-bit integer range [-231, 231 - 1], then return 0.
Assume the environment does not allow you to store 64-bit integers (signed or unsigned).

Example 1:

Input: x = 123
Output: 321

Example 2:
Input: x = -123
Output: -321

Example 3:
Input: x = 120
Output: 21

Example 4:
Input: x = 0
Output: 0

Constraints:
-231 <= x <= 231 - 1
'''
class Solution(object):
    def reverse(self, x):
        # runs through to see if the input is under 32 bits
        x = check32(x)
        
        # converts x into a string
        neg = str(x)
        ans = 0
        
        # determines if it's a neg number or not
        # then runs through the while-loop
        if neg.find("-") == -1:
            ans = revfunc(x, ans)  
        else:
            k = abs(x)
            ans = revfunc(k, ans)
            ans = -ans

        # runs through the check again, 
        # to see if the answer is still under 32 bits
        ans = check32(ans)
        return ans

# check if the input falls under 
# the 32-bit int (-2147483648 < x < 2147483647)
# if not, returns 0
def check32(q):
    if (q < -2147483648):
        return 0
    elif (q > 2147483647):
        return 0
    else:
        return q

# while loop to reverse the string
def revfunc(x, ans):
    while(x != 0):
        curr = x % 10
        x /= 10
        ans = ans * 10 + curr
    return ans