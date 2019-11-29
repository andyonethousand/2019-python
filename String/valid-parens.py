class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []
        
        brackets = {')': '(', '}': '{', ']': '['}
        
        for c in s:
            # if c is a closing bracket
            if c in brackets:
                
                if len(stack) > 0:
                    top_stack = stack.pop()
                else:
                    top_stack = '*'
                
                if top_stack != brackets[c]:
                    return False
            
            else:
                
                stack.append(c)
            
        if len(stack) == 0:
            return True
        else:
            return False