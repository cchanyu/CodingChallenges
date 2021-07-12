'''
Given the head of a sorted linked list, delete all duplicates such that each element appears only once. Return the linked list sorted as well.

Example 1:
Input: head = [1,1,2]
Output: [1,2]

Example 2:
Input: head = [1,1,2,3,3]
Output: [1,2,3]
 

Constraints:
The number of nodes in the list is in the range [0, 300].
-100 <= Node.val <= 100
The list is guaranteed to be sorted in ascending order.
'''
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def deleteDuplicates(self, head):
        # if head is empty, return nothing
        if not head:
            return None
        
        # sets the pointer to the head
        curr = head
        
        # while there's a value
        # compare it to the value after, if it's a match, it skips
        # if it's not a match, sets a new head
        while curr.next:
            if (curr.val == curr.next.val):
                curr.next = curr.next.next
            else:
                curr = curr.next
                
        return head