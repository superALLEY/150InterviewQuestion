
# Best Time to Buy and Sell Stock II

## Problem Description

**Objective:**  
You are given an integer array `prices` where `prices[i]` is the price of a given stock on the `i`th day. On each day, you may decide to buy and/or sell the stock. You can only hold at most one share of the stock at any time. However, you can buy it and then immediately sell it on the same day. The goal is to find and return the maximum profit you can achieve.

**Constraints:**
- The array `prices` contains prices of stocks for each day.
- You are allowed to make multiple transactions, but you can only hold one share of the stock at any time.
- You can buy and then immediately sell the stock on the same day.

**Example:**

- **Input:** `prices = [7, 1, 5, 3, 6, 4]`  
  **Output:** `7`  
  **Explanation:** Buy on day 2 (price = 1) and sell on day 3 (price = 5), profit = 5-1 = 4.  
  Then buy on day 4 (price = 3) and sell on day 5 (price = 6), profit = 6-3 = 3.  
  Total profit is 4 + 3 = 7.

- **Input:** `prices = [1, 2, 3, 4, 5]`  
  **Output:** `4`  
  **Explanation:** Buy on day 1 (price = 1) and sell on day 5 (price = 5), profit = 5-1 = 4.  
  Total profit is 4.

## Approach

### Greedy Algorithm

This problem can be efficiently solved using a greedy approach. The idea is to accumulate the profit from every increase in stock price. The algorithm iterates through the price list and adds the difference between consecutive days where a profit can be made.

1. **Initialization:**  
   - Start with `max_profit = 0`.

2. **Iteration:**
   - Iterate through the prices array starting from the second day.
   - If the current day's price is higher than the previous day's, add the difference to `max_profit`.

3. **Result:**  
   - The total value of `max_profit` will be the maximum profit that can be achieved.

```python
class Solution(object):
    def maxProfit(self, prices):
        max_profit = 0
        
        # Iterate through the prices array
        for i in range(1, len(prices)):
            # If the price on the current day is higher than the previous day,
            # we add the difference to max_profit
            if prices[i] > prices[i - 1]:
                max_profit += prices[i] - prices[i - 1]
        
        return max_profit
```

### Example Walkthrough with `prices = [7, 1, 5, 3, 6, 4]`:

- **Initialization:**  
  Start with `max_profit = 0`.

- **Iteration:**
  - From day 2 to day 3: Profit is 4 (buy at 1, sell at 5)
  - From day 4 to day 5: Profit is 3 (buy at 3, sell at 6)

- **Final Output:**  
  The algorithm returns `7` as the maximum profit.

### Complexity Analysis

- **Time Complexity:** `O(n)` where `n` is the number of elements in the `prices` array. The algorithm iterates through the array once.
- **Space Complexity:** `O(1)` since only a few extra variables are used.

## How to Use This Repository

1. **Clone the Repository:**  
   `git clone https://github.com/superALLEY/150InterviewQuestions.git`

2. **Navigate to the Problem Folder:**  
   Locate the folder for the "Best Time to Buy and Sell Stock II" problem.

3. **Run the Solution:**  
   Open the solution file in your preferred IDE and execute it to see the results.

## Contributing

Contributions are always welcome! To contribute:

1. **Fork the Repository.**
2. **Create a New Branch:**  
   `git checkout -b feature/problem-name`

3. **Commit Your Changes:**  
   `git commit -am 'Add problem-name solution'`

4. **Push to the Branch:**  
   `git push origin feature/problem-name`

5. **Create a Pull Request.`**

## License

This repository is licensed under the MIT License. You are free to use the code for learning and interview preparation.
