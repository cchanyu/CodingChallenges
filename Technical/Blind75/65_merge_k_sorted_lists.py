'''
https://leetcode.com/problems/merge-k-sorted-lists/
'''
class Solution:
  def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
      pq = []
      for i in lists:
          while i != None:
              heapq.heappush(pq, i.val)
              i = i.next
        
      ans = ListNode(-1) 
      cur = ans  
      while pq:
          t = ListNode(heapq.heappop(pq))
          cur.next = t
          cur = cur.next
            
      return ans.next