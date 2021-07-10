'''
Given a sorted array of distinct integers and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.
You must write an algorithm with O(log n) runtime complexity.

Example 1:
Input: nums = [1,3,5,6], target = 5
Output: 2

Example 2:
Input: nums = [1,3,5,6], target = 2
Output: 1

Example 3:
Input: nums = [1,3,5,6], target = 7
Output: 4

Example 4:
Input: nums = [1,3,5,6], target = 0
Output: 0

Example 5:
Input: nums = [1], target = 0
Output: 0

Constraints:
1 <= nums.length <= 104
-104 <= nums[i] <= 104
nums contains distinct values sorted in ascending order.
-104 <= target <= 104
'''
class Solution(object):
    def searchInsert(self, nums, target):
        print(nums, target)
        ans = 0
        i = 0
        length = len(nums)
        
        while(i < length):
            print('i',i,'nums',nums[i],'target',target)
            if(target == nums[i]):
                ans = i
                print('target found',ans)
                break
            elif(target >= nums[i] and i == (length - 1)):
                ans = i + 1
                print('new high num',ans)
                break
            elif(target >= nums[i]):
                ans = i
                print('saved position',ans)
            elif(target < nums[i]):
                ans = i 
                print('else',ans)
                break
            i = i + 1
        print('ans',ans)
        return ans