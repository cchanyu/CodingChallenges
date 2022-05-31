nums = [3, 2, 3]
target = 6

def twoSum(nums, target):
    print(nums, target)
    for i in range(len(nums)):
        j = i + 1
        print(nums[i], nums[j])
        if (nums[i] > target):
            continue
        if (nums[i] + nums[j] == target):
            return [i, j]
    return []

def main():
    sol = twoSum(nums, target)
    print(sol)

if __name__ == '__main__':
    main()