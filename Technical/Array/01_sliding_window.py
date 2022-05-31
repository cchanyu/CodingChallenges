# problem 1
# given an array, find the average of all subarrays of 'k' contiguous elements in it

arr = [1,3,2,6,-1,4,1,8,2]
k = 5

# 1,3,2,6,-1 / 5 (finding the avg)
# 2.2 (avg is appended to the list)

# Brute Force / Naive Approach 
# force calculating all 5 combinations
# Time Complexity: O(N*K)
'''
def find_avg_of_subarr(k, arr):
    ans=[]

    for i in range(len(arr)-k+1): # 0 - (8-5+1) : 0 - 4
        temp = 0

        for j in range(i, i+k): # 0 (i, i+5)
            temp += arr[j]

        ans.append(temp / k)

    return ans
'''

# Better approach
# Reducing the k = 5, overlapping is unnecessary
# Time Complexity: O(N)
def find_avg_of_subarr(k, arr):
    ans=[]
    start, temp = 0, 0

    for i in range(len(arr)):
        temp += arr[i]

        if i >= k-1:
            ans.append(temp / k)
            temp -= arr[start]
            start += 1

    return ans


def main():
    result = find_avg_of_subarr(k, arr)
    print("result", result)

main()