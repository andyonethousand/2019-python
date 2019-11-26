class Solution(object):
    def topKFrequent(self, nums, k):
        most_frequent = [item[0] for item in collections.Counter(nums).most_common(k)]
        return most_frequent