class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        if len(matrix) == 0:
            return []
        
        result = []
        left_index = 0
        right_index = len(matrix[0]) -1
        top_index = 0
        bottom_index = len(matrix) -1
        
        while left_index <= right_index  and top_index <= bottom_index:
            
            # move left to right along the top  
            for i in range(left_index, right_index  + 1):
                result.append(matrix[top_index][i])
            
            # move top down one row down the matrix
            top_index += 1 
            
            # move top to bottom along the right
            for i in range(top_index, bottom_index + 1):
                result.append(matrix[i][right_index])
            
            # move right in one column in the matrix
            right_index -= 1
            
            # move left to right along the bottom
            if top_index <= bottom_index:
                for i in range(right_index, left_index - 1, -1):
                    result.append(matrix[bottom_index][i])
                
            bottom_index -= 1
             
            # move bottom to top along the left
            if left_index <= right_index:
                for i in range(bottom_index, top_index - 1, -1):
                    result.append(matrix[i][left_index])
            
            left_index += 1
                
        return result