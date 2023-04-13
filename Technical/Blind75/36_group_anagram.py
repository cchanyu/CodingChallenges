'''
https://leetcode.com/problems/group-anagrams/
'''
class Solution:
  def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
      dct = defaultdict(list)
        
      for s in strs:
          tracker = [0] * 26
            
          for c in s:
              tracker[ord(c) - ord('a')] += 1
                
          k = tuple(tracker)
          dct[k].append(s)

      return dct.values()