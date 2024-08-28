
# Max Profit from Stock Prices

## Problem Description

Given an array `prices` where `prices[i]` is the price of a given stock on the `i-th` day, return the maximum profit you can achieve from buying and selling the stock. You must buy before you sell, and you are only allowed to complete at most one transaction (i.e., buy one and sell one share of the stock).

If no profit can be achieved, return 0.

### Constraints
- `1 <= prices.length <= 10^5`
- `0 <= prices[i] <= 10^4`

## Example 1

**Input**:
```python
prices = [7, 1, 5, 3, 6, 4]
```
**Output**:
```python
5
```
**Explanation**:
Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6 - 1 = 5.

## Example 2

**Input**:
```python
prices = [7, 6, 4, 3, 1]
```
**Output**:
```python
0
```
**Explanation**:
In this case, no transaction is done, and the maximum profit is 0.

## Approach

### Initial Setup:

- Use a variable `min_price` to keep track of the minimum price encountered so far.
- Use another variable `max_profit` to store the maximum profit encountered so far.

### Iterating Over the Array:

- Iterate through the `prices` array.
- For each price, if it's lower than the current `min_price`, update `min_price`.
- Otherwise, calculate the profit by subtracting `min_price` from the current price, and update `max_profit` if this profit is higher than the current `max_profit`.

### Final Steps:

- After completing the loop, return `max_profit`.

## Solution

```python
class Solution(object):
    def maxProfit(self, prices):
        min_price = float('inf')  # Initialize to a very large number
        max_profit = 0  # Initialize to 0

        for price in prices:
            # Update min_price if current price is lower
            if price < min_price:
                min_price = price
            # Calculate profit if current price is sold at min_price, update max_profit if higher
            elif price - min_price > max_profit:
                max_profit = price - min_price

        return max_profit
```

## Explanation

- The loop goes through each element of the `prices` array.
- If the price is lower than `min_price`, it updates `min_price`.
- Otherwise, it calculates the profit by subtracting `min_price` from the current price and updates `max_profit` if this profit is higher.
- The function returns `max_profit`, which is the maximum profit possible with one transaction.

## Complexity Analysis

- **Time Complexity**: `O(n)`, where `n` is the number of elements in the `prices` array.
- **Space Complexity**: `O(1)`, since we are using only a few variables for calculations and no extra space.

## Additional Notes

This problem tests your ability to implement an efficient algorithm that can find the maximum profit with a single transaction by tracking the minimum price seen so far and calculating possible profits on the fly. It is a common problem in coding interviews as it checks both logical thinking and the ability to optimize algorithms.
