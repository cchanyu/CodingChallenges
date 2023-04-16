'''
https://leetcode.com/problems/linked-list-cycle/
'''
class Solution:
  def hasCycle(self, head: Optional[ListNode]) -> bool:
      if head == None or head.next == None:
          return False
        
      fast, slow = head, head
        
      while fast != None and fast.next != None:
          slow = slow.next
          fast = fast.next.next
            
          if slow == fast:
              return True
        
      return False