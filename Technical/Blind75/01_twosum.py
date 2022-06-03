'''
two sum can not use sliding window technique,
because it's not a sorted array.

two sum needs to use dict
and check whether there's a match
'''

from collections import defaultdict


nums = [3, 2, 3]
target = 6

def twoSum(nums, target):
    lookup = defaultdict(list)
    for i, v in enumerate(nums):
        temp = target - v # 6 - 3 = 3 temp
        if temp in lookup: # if 3 in dict
            return [lookup[temp][0],i] # return both
        lookup[v].append(i) # otherwise add value to dict
    return None


def main():
    sol = twoSum(nums, target)
    print(sol)

if __name__ == '__main__':
    main()