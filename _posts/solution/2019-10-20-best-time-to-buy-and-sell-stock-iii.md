---
title: 买卖股票的最佳时机 III
qid: 123
tags: [数组,动态规划]
---


- 难度： 困难
- 通过率： 32.4%
- 题目链接：[https://leetcode.com/problems/best-time-to-buy-and-sell-stock-iii](https://leetcode.com/problems/best-time-to-buy-and-sell-stock-iii)


## 题目描述

来源于 [https://leetcode-cn.com/](https://leetcode-cn.com/)

<p>给定一个数组，它的第<em> i</em> 个元素是一支给定的股票在第 <em>i </em>天的价格。</p>

<p>设计一个算法来计算你所能获取的最大利润。你最多可以完成&nbsp;<em>两笔&nbsp;</em>交易。</p>

<p><strong>注意:</strong>&nbsp;你不能同时参与多笔交易（你必须在再次购买前出售掉之前的股票）。</p>

<p><strong>示例&nbsp;1:</strong></p>

<pre><strong>输入:</strong> [3,3,5,0,0,3,1,4]
<strong>输出:</strong> 6
<strong>解释:</strong> 在第 4 天（股票价格 = 0）的时候买入，在第 6 天（股票价格 = 3）的时候卖出，这笔交易所能获得利润 = 3-0 = 3 。
&nbsp;    随后，在第 7 天（股票价格 = 1）的时候买入，在第 8 天 （股票价格 = 4）的时候卖出，这笔交易所能获得利润 = 4-1 = 3 。</pre>

<p><strong>示例 2:</strong></p>

<pre><strong>输入:</strong> [1,2,3,4,5]
<strong>输出:</strong> 4
<strong>解释:</strong> 在第 1 天（股票价格 = 1）的时候买入，在第 5 天 （股票价格 = 5）的时候卖出, 这笔交易所能获得利润 = 5-1 = 4 。 &nbsp; 
&nbsp;    注意你不能在第 1 天和第 2 天接连购买股票，之后再将它们卖出。 &nbsp; 
&nbsp;    因为这样属于同时参与了多笔交易，你必须在再次购买前出售掉之前的股票。
</pre>

<p><strong>示例 3:</strong></p>

<pre><strong>输入:</strong> [7,6,4,3,1] 
<strong>输出:</strong> 0 
<strong>解释:</strong> 在这个情况下, 没有交易完成, 所以最大利润为 0。</pre>


## 解法：

计算在 i 天前能获得的最大收益，和在 i 天后能够获得的最大收益。如此，计算 i 天之前和之后的收益和，得出最大收益。

```python
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) < 2:
            return 0
        
        profit_before = []
        profit_after = [] 
        
        min_price = float('inf')
        for price in prices:
            min_price = min(min_price, price)
            max_profit = max(max_profit, price - min_price)
            profit_before.append(max_profit)

        max_price = float('-inf')
        for price in reversed(prices):
            max_price = max(max_price, price)
            max_profit = max(max_profit, max_price - price)
            profit_after.append(max_profit)
        profit_after = reversed(profit_after)
        
        profit = map(lambda x: x[0] + x[1], zip(profit_before, profit_after))
        max_profit = max(profit)

        return max_profit
```