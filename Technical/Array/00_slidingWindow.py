# problem 0
# find the max sum of array and return it

arr = [2,1,5,1,3,2] # output = 9, [5,1,3]
k = 3

# Brute Force / Naive Approach
# iters through all the possibility
'''
def max_sum_of_arr(arr, k):
    ans = 0
    for i in range(len(arr) - k + 1): # +1 on nested forloops
        temp = 0
        for j in range(i, i + k):
            temp += arr[j] # always don't forget to do arr[j] not j
        ans = max(ans, temp)
    return ans
'''

# Sliding Window approach
# WRONG?? IDK
def max_sum_of_arr(arr, k):
    ans, temp, start = 0, 0, 0
    
    for i in range(k): # 0 - 2 (3 total)
        temp += arr[i]
        ans = temp

        for j in range(k + 1, len(arr)): # 4 - 7 (3 total) range(start, stop, step)
            temp = temp + arr[j] - arr[j-k]
            print('temp:', temp, 'val:', arr[j], 'idx:', j)
            ans = max(ans, temp)
    
    return ans


def main():
    result = max_sum_of_arr(arr, k)
    print('result', result)

main()