class Solution:
    def missingNumber(self, nums):
        num_set = set(nums)
        
        for n in range(len(nums) + 1):
            if n not in num_set:
                return n
            