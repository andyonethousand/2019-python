class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        arr_2d = [[False for _ in range(len(s))] for _ in range(len(s))]
        
        max_sub_len = 0
        substring = (0, 0)
        
        # One character case
        for i in range(len(s)):
            arr_2d[i][i] = True
        
        # Two characters case
        for i in range(len(s) - 1):
            j = i + 1
            if s[i] == s[j]:
                arr_2d[i][j] = True
                max_sub_len = 2
                substring = (i, j)
                       
        # General case
        for step in range(2, len(s)):
            i = 0 
            j = i + step
            while (j < len(s)):
                if (s[i] == s[j]) and arr_2d[i + 1][j - 1]:
                    arr_2d[i][j] = True
                if arr_2d[i][j] == True and (j - i + 1) > max_sub_len:
                    max_sub_len = j - i + 1
                    substring = (i, j)
        
                i += 1
                j += 1
            
        return s[substring[0]: substring[1] + 1]