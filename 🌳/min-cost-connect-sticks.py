class Solution:
    def connectSticks(self, sticks: List[int]) -> int:
        
        heapq.heapify(sticks)
        cost = 0
                
        while len(sticks) > 1:
            val = heapq.heappop(sticks) + heapq.heappop(sticks)
            cost += val
            heapq.heappush(sticks, val)
        
        return cost 
        
        
        
 