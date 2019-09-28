class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash_table = dict()
        
        for i in range(len(nums)):
            hash_table[nums[i]] = i
        
        for i in range(len(nums)):
            number_to_get = target - nums[i]
            if number_to_get in hash_table and i != hash_table[number_to_get]:
                return [i, hash_table[number_to_get]]