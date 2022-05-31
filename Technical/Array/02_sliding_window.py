# problem 2
# given an array of positive number

arr = [2,1,5,1,3,2] # output = 9, [5,1,3]
arr2 = [2,3,4,1,5] # output = 7, [3,4]
k = 3

# Brute force approach
'''
def max_sum_of_arr(arr, k):
    ans = 0
    for i in range(len(arr) - k + 1): # 0 - (5-3+1) +1 is always needed for nested forloop (aka 2 forloops)
        temp = 0 
        for j in range(i, i+k):
            temp += arr[j]
        ans = max(ans, temp)
    return ans
'''

# Better approach
# same concept, basically slide moves
def max_sum_of_arr(arr, k):
    ans, temp, start = 0, 0, 0

    for i in range(len(arr)):
        temp += arr[i]

        if i >= k-1:
            ans = max(ans, temp)
            temp -= arr[start]
            start += 1

    return ans

def main():
    result = max_sum_of_arr(arr, 3)
    print('result', result)

main()