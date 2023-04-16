'''
https://leetcode.com/problems/remove-nth-node-from-end-of-list/
'''
class Solution:
  def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
      if head.next == None:
          return None
        
      f, s = head, head
        
      while n:
          f = f.next
          n -= 1
            
      if f == None:
          return head.next
        
      while f != None and f.next != None:
          s = s.next
          f = f.next
            
      s.next = s.next.next

      return head    