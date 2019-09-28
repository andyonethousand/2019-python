class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        hash_set = set()
        if (len(nums)) == 0:
            return False
        
        for i in range(len(nums)):
            if nums[i] not in hash_set:
                hash_set.add(nums[i])
            else:
                return True
        return False
        