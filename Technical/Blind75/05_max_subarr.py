'''
leet code suggestion: try divide and conquer approach, it's more subtle with recursion
'''

nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4] # output: 6 [4, -1, 2, 1]

def maxSubArray(nums):
    currentSum = nums[0]
    maxSum = nums[0]

    for i in range(len(nums)):
        if currentSum >= 0:
            currentSum += nums[i]
        else:
            currentSum = nums[i]
        maxSum = max(currentSum, maxSum)
    return maxSum

def main():
    sol = maxSubArray(nums)
    print(sol)

if __name__ == '__main__':
    main()