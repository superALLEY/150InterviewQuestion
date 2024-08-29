class CryptoTrader:
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        max_profit = 0
        
        # Iterate through the prices array starting from the second day
        for i in range(1, len(prices)):
            # If today's price is higher than yesterday's, calculate the profit
            if prices[i] > prices[i - 1]:
                # Add the profit from this transaction
                max_profit += prices[i] - prices[i - 1]
        
        return max_profit

# Example usage:
if __name__ == "__main__":
    # Example prices for a cryptocurrency over a series of days
    prices = [7, 1, 5, 3, 6, 4]

    trader = CryptoTrader()
    profit = trader.maxProfit(prices)
    
    print(f"The maximum profit from trading is: {profit}")
