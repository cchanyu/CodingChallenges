
'''
correct ans, but time exceeded in a large input, time complexity is at least n^2
'''
import math
from pickletools import read_unicodestringnl


nums = [1,2,3,4] # [24,12,8,6]
nums2 = [-1,1,0,-3,3] # [0,0,9,0,0]

def productExceptSelf(nums):
    idx1 = 0
    ans = []
    for i in range(len(nums)):
        idx1 = i

        select1 = nums[:idx1]
        select2 = nums[idx1+1:]

        # prod1 = math.prod(select1)
        # prod2 = math.prod(select2)
        prod1 = 1
        for j in select1:
            prod1 *= j
        prod2 = 1
        for k in select2:
            prod2 *= k

        ans.append(prod1 * prod2)
    return ans
        

def main():
    sol = productExceptSelf(nums)
    print(sol)

if __name__ == '__main__':
    main()