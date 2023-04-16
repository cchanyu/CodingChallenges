'''
https://leetcode.com/problems/reorder-list/
'''
class Solution:
  def reorderList(self, head: Optional[ListNode]) -> None:
      if head == None or head.next == None:
          return
        
      pre = None
      fast, slow = head, head
        
      while fast != None and fast.next != None:
          fast = fast.next.next
          pre = slow
          slow = slow.next

      pre.next = None
        
      cur = slow
      pre = None
      while cur != None:
          nxt = cur.next
          cur.next = pre
          pre = cur
          cur = nxt
            
      self.flag = False
        
      def merge(a, b):
          if a == None or b == None:
              return b if a == None else a
          self.flag = not self.flag
            
          if self.flag:
              a.next = merge(a.next, b)
              return a
          else:
              b.next = merge(a, b.next)
              return b
            
      merge(head, pre)