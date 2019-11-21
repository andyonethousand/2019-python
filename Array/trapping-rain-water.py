class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        left_iterator = 0
        right_iterator = len(height) - 1
        leftMax, rightMax, result = 0, 0,0
        
        while left_iterator <= right_iterator:
            leftMax = max(leftMax, height[left_iterator])
            rightMax = max(rightMax, height[right_iterator])
            
            if leftMax < rightMax:
                result += leftMax - height[left_iterator]
                left_iterator += 1
            else:
                result += rightMax - height[right_iterator]
                right_iterator -= 1
            
        return result
        
        