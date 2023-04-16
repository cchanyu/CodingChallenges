'''
https://leetcode.com/problems/binary-tree-maximum-path-sum/
'''
class Solution:
  def maxPathSum(self, root: Optional[TreeNode]) -> int:
      self.ans = float('-inf')
        
      def dfs(node):
          if node == None:
              return 0
            
          l, r = dfs(node.left), dfs(node.right)
          self.ans = max(self.ans, l + r + node.val)
            
          return max(0, max(l, r) + node.val)    
            
      dfs(root)
      return self.ans