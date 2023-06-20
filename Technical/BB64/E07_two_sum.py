def twoSum(self, nums, target):
    list = {}
    for i, v in enumerate(nums):
        temp = target - v
        if temp in list:
            return [i, list[temp]]
        list[v] = i
    return None

'''
nums: [3, 4, 5]
target: 9
output: [1,2]


create a list
iter thru nums:
temp val caluclates
if that temp val exist in the list, return

'''