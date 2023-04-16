'''
https://leetcode.com/problems/clone-graph/
'''
class Solution:
  def __init__(self):
      self.vis = {}
        
  def cloneGraph(self, node: 'Node') -> 'Node':
        
      if node == None:
          return None
        
      if node in self.vis:
          return self.vis[node]
        
      cloneNode = Node(node.val, [])
        
      self.vis[node] = cloneNode
        
      for child in node.neighbors:
          cloneNode.neighbors.append(self.cloneGraph(child))
            
      return cloneNode 