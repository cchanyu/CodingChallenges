def twoSum(self, nums, target):
    list = {}
    for i, v in enumerate(nums):
        temp = target - v
        if temp in list:
            return [i, list[temp]]
        list[v] = i
    return None
