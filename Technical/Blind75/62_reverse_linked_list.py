'''
https://leetcode.com/problems/reverse-linked-list/
'''
class Solution:
  def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
      if head == None or head.next == None:
          return head
        
      pre = None
      cur = head
      nxt = None
        
      while cur != None:
          nxt = cur.next
          cur.next = pre
          pre = cur
          cur = nxt
        
      return pre 

class Solution:
  def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
      if head == None or head.next == None:
          return head
        
      ans = self.reverseList(head.next)
        
      head.next.next = head
      head.next = None
        
      return ans 