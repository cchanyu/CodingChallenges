'''
https://leetcode.com/problems/kth-smallest-element-in-a-bst/
'''
class Solution:
  def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
      self.ans = None   
      self.k = k
        
      def dfs(node):
            
          if node is None:
              return
            
          dfs(node.left)

          self.k -= 1  
            
          if self.k == 0:
              self.ans = node.val
              return
            
          dfs(node.right)
            
      dfs(root)
      return self.ans