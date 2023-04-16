'''
https://leetcode.com/problems/find-median-from-data-stream/
'''
class MedianFinder:

  def __init__(self):
      self.pqMin = []
      self.pqMax = []

  def addNum(self, num: int) -> None:
      heapq.heappush(self.pqMin, -1 * num)
        
      if self.pqMin and self.pqMax and (-1 * self.pqMin[0] > self.pqMax[0]):
          val = -1 * heapq.heappop(self.pqMin)
          heapq.heappush(self.pqMax, val)
            
      if len(self.pqMin) > len(self.pqMax) + 1:
          val = -1 * heapq.heappop(self.pqMin)
          heapq.heappush(self.pqMax, val)
        
      if len(self.pqMax) > len(self.pqMin) + 1:
          val = heapq.heappop(self.pqMax)
          heapq.heappush(self.pqMin, -1 * val)

  def findMedian(self) -> float:
      if len(self.pqMin) > len(self.pqMax):
          return -1 * self.pqMin[0]
        
      if len(self.pqMax) > len(self.pqMin):
          return self.pqMax[0]
        
      return (-1 * self.pqMin[0] + self.pqMax[0]) / 2