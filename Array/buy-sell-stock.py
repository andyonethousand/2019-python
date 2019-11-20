class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        i = 0
        j = 1
        m_price = 0
        
        while j < len(prices):
            if prices[j] < prices[i]:
                i += 1 
                j = i + 1
            else:
                profit = prices[j] - prices[i]
                if profit > m_price:
                    m_price = profit
                j += 1
        
        return m_price
            