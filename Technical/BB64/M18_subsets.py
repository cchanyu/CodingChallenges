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