class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = ''.join(filter(str.isalnum, s))
        s = s.replace(' ', '')
        s = s.lower()
        
        if s[::-1] == s:
            return True
        else:
            return False

      
        
