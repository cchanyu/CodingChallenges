"""
Merge two sorted linked lists and return it as a sorted list. The list should be made by splicing together the nodes of the first two lists.

Example 1:
Input: l1 = [1,2,4], l2 = [1,3,4]
Output: [1,1,2,3,4,4]

Example 2:
Input: l1 = [], l2 = []
Output: []

Example 3:
Input: l1 = [], l2 = [0]
Output: [0]

Constraints:
The number of nodes in both lists is in the range [0, 50].
-100 <= Node.val <= 100
Both l1 and l2 are sorted in non-decreasing order.
"""

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeTwoLists(self, l1, l2):
        dummy = ListNode()
        tail = dummy
        
        # while l1 and l2 are active
        while l1 and l2:
            # compare values: if l2 is bigger than l1
            if l1.val < l2.val:
                # l1 is added to the list
                tail.next = l1
                # update the l1 w/ new val
                l1 = l1.next
            else:
                # l2 is added if it's equal or smaller
                tail.next = l2
                # update the l2 w/ new val
                l2 = l2.next
            # update the tail
            tail = tail.next
        
        # if either l1 or l2 is null, but the other isn't
        if l1:
            # put the rest of the node into the tail
            tail.next = l1
        elif l2:
            # put the rest of the node into the tail
            tail.next = l2
        
        return dummy.next
                