def trap(self, height):
    ans = 0
    n = len(height)
    left, right = 0, n-1
    left_max, right_max = height[left], height[right]

    while left < right:
        left_max = max(left_max, height[left])
        right_max = max(right_max, height[right])

        if left_max <= right_max:
            ans += left_max - height[left]
            left += 1
        else:
            ans += right_max - height[right]
            right -= 1
        
        return ans

'''
Intuition: have the pointer and calculate left and right of it. if it's greater than its pointer, it's able to be trapped
better sol: having two pointer, saves time of re-itering and computations.

time complexity: O(n)
space complexity: O(1)

Arr: [0 1 0 2 0 1 2 0 0 2 0 0] 
MaxL: [0 1 1 2 2 2 2 2 2 2 2 2] 
MaxR: [2 2 2 2 2 2 2 2 2 2 0 0] # iter thru -1(opp) direction and collect highest 
MinLR: [0 1 1 2 2 2 2 2 2 2 0 0] # whichever is lower between the two
Ans: [0 0 1 0 2 1 0 2 2 0 0 0] # MinLR - Arr = trapped water
'''