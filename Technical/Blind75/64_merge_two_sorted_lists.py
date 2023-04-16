'''
https://leetcode.com/problems/merge-two-sorted-lists/
'''
class Solution:
  def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
      if list1 == None or list2 == None:
          return list2 if list1 == None else list1
        
      if list1.val <= list2.val:
          list1.next = self.mergeTwoLists(list1.next, list2)
          return list1
        
      list2.next = self.mergeTwoLists(list1, list2.next)
      return list2