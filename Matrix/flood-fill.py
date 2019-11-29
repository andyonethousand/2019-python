class Solution(object):
    def floodFill(self, image, sr, sc, newColor):
        """
        :type image: List[List[int]]
        :type sr: int
        :type sc: int
        :type newColor: int
        :rtype: List[List[int]]
        """
        
        color = image[sr][sc]
        
        if color == newColor:
            return image
        
        self.dfs(sr, sc, image, newColor, color)
        
        return image

    def dfs(self, i, j , image, newColor, color):
            if i < 0 or j < 0 or i >= len(image) or j >= len(image[0]) or image[i][j] != color:
                return None
            
            image[i][j] = newColor
            
            self.dfs(i + 1, j, image, newColor, color)
            self.dfs(i - 1, j, image, newColor, color)
            self.dfs(i, j + 1, image, newColor, color)
            self.dfs(i, j - 1, image, newColor, color)
            
