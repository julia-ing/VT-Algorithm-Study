class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        s = ''.join(c for c in s if c.isalnum())

        for idx in range(len(s)//2):
            if s[idx] != s[len(s)-1-idx]: return False
        
        return True
      
      
# Deque
class Solution:
    def isPalindrome(self, s: str) -> bool:
      # 자료형 Deque로 선언
      strs: Deque = collections.deque()
        
      for char in s:
        if char.isalnum():
          strs.append(char.lower())
          
      while len(strs) > 1:
        if strs.popleft() != strs.pop():
          return False
        
      return True
    
# Slicing
class Solution:
    def isPalindrome(self, s: str) -> bool:
      s = s.lower()
      
      # 정규식으로 불필요한 문자 필터링
      s = re.sub('[^a-z0-9]', '', s)
      
      # 슬라이싱
      return s == s[::-1]
