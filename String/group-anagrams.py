class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        # list for each value because you don't want to overwrite the individual
        # words which will eventually be returned as the solution
        hash_table = collections.defaultdict(list)
        
        # have to use string because a list can't be a key
        # you could have used something like tuple too
        for i in strs:
            hash_table[str(sorted(i))].append(i)
        
        return hash_table.values()
    
