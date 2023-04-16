'''
https://leetcode.com/problems/invert-binary-tree/
'''
class Solution:
  def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
      if root is None:
          return None
            
      temp = self.invertTree(root.right)
      root.right = self.invertTree(root.left)
      root.left = temp
        
      return root