'''
you could use a set() and do .add(i), while checking if it's there
or 
you could use dict() and .append(i), while checking if it's there

set() seems to be more efficient
'''
from collections import defaultdict


nums = [1,2,3,1] # true
nums2 = [1,2,3,4] # false

def containsDuplicate(nums):
    check = defaultdict(list)
    for i, v in enumerate(nums):
        if v in check:
            return True
        check[v].append(nums[i])
    return False

def main():
    sol = containsDuplicate(nums)
    print(sol)

if __name__ == '__main__':
    main()