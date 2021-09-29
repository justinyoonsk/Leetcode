class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price = float("inf")
        max_price = float("-inf")
        
        for i in range(len(prices)):
            min_price = min(prices[i], min_price)
            
            max_price = max(max_price, prices[i] - min_price)
            
        return max_price
            
    # O(N) time
    # O(1) space
