'''
Write an algorithm to determine if a number n is happy.
A happy number is a number defined by the following process:
Starting with any positive integer, replace the number by the sum of the squares of its digits.
Repeat the process until the number equals 1 (where it will stay), or it loops endlessly in a cycle which does not include 1.
Those numbers for which this process ends in 1 are happy.
Return true if n is a happy number, and false if not.

Example 1:
Input: n = 19
Output: true

Explanation:
12 + 92 = 82
82 + 22 = 68
62 + 82 = 100
12 + 02 + 02 = 1

Example 2:
Input: n = 2
Output: false
 
Constraints:
1 <= n <= 231 - 1
'''
class Solution(object):
    def isHappy(self, n):
        q = 0
        ans = recurr(n, q)
        return ans

# recursive function
def recurr(n, q):
    nstr = str(n)
    length = len(nstr)
    nlist, hold = [], []
    ans = False
    i,nsum = 0,0
    q += 1

    if n == 1:
        ans = True
        return ans
    elif q == 30:
        return ans
    else:
        while length:
            nstr.split()
            nlist.append(nstr[i])
            length -= 1
            i += 1

        for k in nlist:
            k = int(k)
            hold.append(k**2)
        
        for h in hold:
            nsum += h
        
        return recurr(nsum, q)