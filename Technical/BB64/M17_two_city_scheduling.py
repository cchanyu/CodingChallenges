class Solution(object):
    def twoCitySchedCost(self, costs):
        res = 0
        
        for cost in costs:
            res += min(cost)

        return res

'''
greedy algorithm question


'''