class Solution(object):
    def sortArray(self, nums):
        self.quickSort(nums, 0, len(nums) - 1)
        return nums
    
    def quickSort(self, nums, l, h):
        if h <= l:
            return 

        # choose pivot
        mid = (l + h) / 2
        pivot = nums[mid]
        
        l_index, h_index = l, h
        
        while l_index <= h_index:
            
            # keep moving l_index and h_index amongst the array, as long as the correct
            # conditions are met (everything left of pivot must be smaller, everything
            # right of pivot must be larger)
            
            # if one of these rules is violated, stop moving
            
            while l_index <= h_index and nums[l_index] < pivot:
                l_index += 1
            while l_index <= h_index and nums[h_index] > pivot:
                h_index -= 1

            # once l_index and h_index both stop moving, swap the respective values at 
            # l_index and h_index
            
            if l_index <= h_index:
                nums[l_index], nums[h_index] = nums[h_index], nums[l_index]
                
                # set bounds for the sub-arrays soon to be quicksorted
                
                l_index += 1
                h_index -= 1
        
        # quicksort the sub-arrays
        
        self.quickSort(nums, l, h_index)
        self.quickSort(nums, l_index, h)
        
        