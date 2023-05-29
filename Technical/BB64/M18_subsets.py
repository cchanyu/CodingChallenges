def subsets(self, nums):
    list = []
    
    # DFS(?)/Backtracking
    def backtrack(i, temp):
        if i == len(nums):
            list.append(temp[:])
            return
        else:
            # recursive, DFS
            backtrack(i+1, temp+[nums[i]])
            backtrack(i+1, temp)
    backtrack(0, [])
    return list

'''
input: [1,2,3]
subsets: [[], [1], [2], [3], [1,2], [1,3], [2,3], [1,2,3]]
'''