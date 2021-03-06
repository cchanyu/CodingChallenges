'''
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
You may assume that each input would have exactly one solution, and you may not use the same element twice.
You can return the answer in any order.

Example 1:
Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Output: Because nums[0] + nums[1] == 9, we return [0, 1].

Example 2:
Input: nums = [3,2,4], target = 6
Output: [1,2]

Example 3:
Input: nums = [3,3], target = 6
Output: [0,1]

Constraints:
2 <= nums.length <= 104
-109 <= nums[i] <= 109
-109 <= target <= 109
Only one valid answer exists.
'''
class Solution(object):
    def twoSum(self, nums, target):
        ans = []
        length = len(nums)
        for i in range(length):
            for j in range(i+1, length):
                if(nums[i] + nums[j] == target):
                    ans.append(i)
                    ans.append(j)
        return ans

'''
class Solution(object):
    def twoSum(self, nums, target):
        for ind1, num1 in enumerate(nums):
            for ind2, num2 in enumerate(nums[(ind1 + 1):]):
                if (num1 + num2) == target:
                    return [ind1, (ind2 + ind1 + 1)]
'''