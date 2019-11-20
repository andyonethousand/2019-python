class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0:
            return 0
        
        if len(s) == 1:
            return 1
        
        i = 0
        j = 1
        count = 0
        curr_c = 1
        h = set()
        
        while i < len(s) and j < len(s):
            h.add(s[i])
            if s[j] not in h:
                h.add(s[j])
                curr_c += 1
                if curr_c > count:
                    count = curr_c
                j += 1
        
            else:
                h.clear()
                i += 1
                j = i + 1
                curr_c = 1
                if curr_c > count:
                    count = curr_c
        
        return count