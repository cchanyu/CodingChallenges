'''
https://leetcode.com/problems/subtree-of-another-tree/
'''
class Solution:
  def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:            
      if self.sameTree(root, subRoot):
          return True
        
      return (root.left != None and self.isSubtree(root.left, subRoot)) or (root.right != None and self.isSubtree(root.right, subRoot))
    
    
  def sameTree(self, a, b):
      if a == None and b == None:
          return True

      return a != None and b != None and a.val == b.val and self.sameTree(a.left, b.left) and self.sameTree(a.right, b.right)