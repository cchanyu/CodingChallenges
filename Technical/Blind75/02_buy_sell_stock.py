'''
loop through the list
and use temp to learn the profit
if the profit is greater than existing max, replace it
also if min price is lower, replace it
'''

from collections import defaultdict
from traitlets import default


prices = [7,1,5,3,6,4] # output: 5
prices2 = [7,6,4,3,1] # output: 0

def maxProfit(prices):
    max_profit = 0
    min_price = prices[0]
    for i,v in enumerate(prices):
        profit = prices[i] - min_price # temp profit
        max_profit = max(profit, max_profit) # comparing to existing profit
        min_price = min(min_price, prices[i]) # comparing the min price
    return max_profit

def main():
    sol = maxProfit(prices)
    print(sol)

if __name__ == '__main__':
    main()