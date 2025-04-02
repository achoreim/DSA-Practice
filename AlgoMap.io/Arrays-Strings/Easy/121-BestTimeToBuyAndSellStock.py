"""
Easy
121. Best Time to Buy and Sell Stock
https://leetcode.com/problems/best-time-to-buy-and-sell-stock/description/

Time to solve: 
"""

"""
Problem Description:
You are given an array prices where prices[i] is the price of a given stock on the ith day.

You want to maximize your profit by choosing a single day to buy one stock and choosing a
different day in the future to sell that stock.

Return the maximum profit you can achieve from this transaction. If you cannot achieve any
profit, return 0.

 

Example 1:

Input: prices = [7,1,5,3,6,4]
Output: 5
Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
Note that buying on day 2 and selling on day 1 is not allowed because you must buy before you sell.
Example 2:

Input: prices = [7,6,4,3,1]
Output: 0
Explanation: In this case, no transactions are done and the max profit = 0.
 

Constraints:

1 <= prices.length <= 105
0 <= prices[i] <= 104
"""

"""
My First Solution: Brute Force

Solution not accepted: Time Limit Exceeded
"""

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0

        for x in range( 0, len(prices)):
            for y in prices[x:]:
                if y-prices[x] > profit:
                    profit = y- prices[x]

        return profit 


"""
AI Solution:

Chat-gpt was able to solve the problem in a O(n) time complexity (As shown bellow):
"""


class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        min = prices[0]
        profit = 0

        for price in prices:
            if price < min:
                min = price
            elif price - min > profit:
                profit = price - min
        

        return profit
    

"""
Notes:

Mistakes: 
    - Was not able to build upon my brute force solution, this is because I failed to spot the 
    patter in which you can update the minimum price, after the fact that the correct profit has been
    calculated already. This misinterpretation could have been avoided if I had run through the problem
    by hand before attempting to solve it.


What to Work on for next time:
    - Make sure that you run through solution by hand before starting to solve the problem

"""