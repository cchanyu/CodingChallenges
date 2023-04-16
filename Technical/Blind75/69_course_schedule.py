'''
https://leetcode.com/problems/course-schedule/
'''
class Solution:
  def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
      ind = [0] * numCourses
        
      for p in prerequisites:
          ind[p[1]] += 1
            
      q = deque()
        
      for i in range(numCourses):
          if ind[i] == 0:
              q.append(i)
                
      g = [0] * numCourses
        
      for i in range(numCourses):
          g[i] = []
            
      for p in prerequisites:
          g[p[0]].append(p[1])
            
      while q:
          numCourses -= 1
            
          u = q.popleft()
          for v in g[u]:
              ind[v] -= 1
              if ind[v] == 0:
                  q.append(v)
                    
      return numCourses == 0