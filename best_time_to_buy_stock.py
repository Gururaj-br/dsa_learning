'''
Best Time to Buy and Sell Stock - Medium
You are given an integer array prices where prices[i] is the price of NeetCoin on the ith day.

You may choose a single day to buy one NeetCoin and choose a different day in the future to sell it.

Return the maximum profit you can achieve. You may choose to not make any transactions, in which case the profit would be 0.

Example 1:

Input: prices = [10,1,5,6,7,1]

Output: 6
Explanation: Buy prices[1] and sell prices[4], profit = 7 - 1 = 6.

Example 2:

Input: prices = [10,8,7,5,2]

Output: 0
Explanation: No profitable transactions can be made, thus the max profit is 0.

Constraints:

1 <= prices.length <= 100
0 <= prices[i] <= 100


Recommended Time & Space Complexity
You should aim for a solution with O(n) time and O(1) space, where n is the size of the input array.
'''

def maxProfit(prices):
    min_price = prices[0]
    profit = 0

    for price in prices:
        current_profit = price - min_price
        profit = max(profit, current_profit)
        min_price = min(min_price, price)
    return profit

# Example usage:
print(maxProfit([10,1,5,6,7,1]))  # 6
print(maxProfit([10,8,7,5,2]))  # 0


'''
The Logic:

Track the minimum price: min_price = prices[0] - Start by assuming the first day's price is the lowest price you've seen so far.

Loop through each day's price: For every day after the first, you calculate:

Current profit: current_profit = price - min_price - How much money would you make if you sold today at the current price, having bought at the lowest price seen so far?
Update best profit: profit = max(profit, current_profit) - Keep track of the best profit you've found so far.
Update minimum price: min_price = min(min_price, price) - If today's price is lower than the lowest you've seen, update it.
Return the answer: After checking all days, return the maximum profit.

Simple Example:
For [10, 1, 5, 6, 7, 1]:

Day 0: min=10, profit=0
Day 1: Price is 1 (new minimum). Profit if sold today = 1-10 = -9. Best profit = 0
Day 2: Price is 5. Profit if sold today = 5-1 = 4. Best profit = 4
Day 3: Price is 6. Profit if sold today = 6-1 = 5. Best profit = 5
Day 4: Price is 7. Profit if sold today = 7-1 = 6. Best profit = 6 ✓
Day 5: Price is 1 (new minimum). Best profit stays = 6
Result: Maximum profit is 6 (buy at 1, sell at 7)
'''