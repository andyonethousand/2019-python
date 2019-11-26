class Solution:
    def reorderLogFiles(self, logs):
        """
        :type logs: List[str]
        :rtype: List[str]
        """
        digits = []
        letters = []
        
        for log in logs:
            if log.split()[1].isdigit():
                digits.append(log)
            else:
                letters.append(log)
        
        letters = sorted(letters, key = lambda x: x.split()[0])
   
        letters = sorted(letters, key = lambda x: x.split()[1:])    
    
        result = letters + digits                                      
        
        return result

