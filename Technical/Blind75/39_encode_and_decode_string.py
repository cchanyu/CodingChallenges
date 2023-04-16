'''
https://leetcode.com/problems/encode-and-decode-strings/
'''
class Codec:
  def encode(self, strs: List[str]) -> str:
      encoded = ''
        
      for s in strs:
          for c in s:
              encoded += str(ord(c)) + ';'        
          encoded += '#'
            
      return encoded

  def decode(self, s: str) -> List[str]:
      decoded = []
        
      for st in s.split('#')[:-1]:
          word = ''
            
          for char in st.split(';')[:-1]:
              word += chr(int(char))
          decoded.append(word)
            
      return decoded