nums = [2,3,-2,4] # output 6 [2,3]

def maxProduct(nums):
    ans = 1
    for i in range(len(nums)):
        if nums[i] == 0:
            continue
        elif nums[i] < 0:
            continue
        else:
            '''
            gotta find 
            '''
            ans *= nums[i]

    return ans

def main():
    sol = maxProduct(nums)
    print(sol)

if __name__ == '__main__':
    main()