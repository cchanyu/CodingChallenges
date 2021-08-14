'''
Write a function to find the longest common prefix string amongst an array of strings.
If there is no common prefix, return an empty string "".

Example 1:
Input: strs = ["flower","flow","flight"]
Output: "fl"

Example 2:
Input: strs = ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.
 
Constraints:
1 <= strs.length <= 200
0 <= strs[i].length <= 200
strs[i] consists of only lower-case English letters.
'''
class Solution(object):
    def longestCommonPrefix(self, strs):
        ans = ""
        i = 0
        
        while True:
            try:
                sets = set(string[i] for string in strs)
                print("sets:", sets)
                if len(sets) == 1:
                    ans += sets.pop()
                    i += 1
                else:
                    break
            except Exception as e:
                break
        return ans
        