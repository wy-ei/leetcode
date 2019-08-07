## 121. Best Time to Buy and Sell Stock

- 难度： 简单
- 通过率： 45.4%
- 题目链接：[https://leetcode.com/problems/best-time-to-buy-and-sell-stock](https://leetcode.com/problems/best-time-to-buy-and-sell-stock)


## 题目描述

来源于 [https://leetcode-cn.com/](https://leetcode-cn.com/)

<p>给定一个数组，它的第&nbsp;<em>i</em> 个元素是一支给定股票第 <em>i</em> 天的价格。</p>

<p>如果你最多只允许完成一笔交易（即买入和卖出一支股票），设计一个算法来计算你所能获取的最大利润。</p>

<p>注意你不能在买入股票前卖出股票。</p>

<p><strong>示例 1:</strong></p>

<pre><strong>输入:</strong> [7,1,5,3,6,4]
<strong>输出:</strong> 5
<strong>解释: </strong>在第 2 天（股票价格 = 1）的时候买入，在第 5 天（股票价格 = 6）的时候卖出，最大利润 = 6-1 = 5 。
     注意利润不能是 7-1 = 6, 因为卖出价格需要大于买入价格。
</pre>

<p><strong>示例 2:</strong></p>

<pre><strong>输入:</strong> [7,6,4,3,1]
<strong>输出:</strong> 0
<strong>解释: </strong>在这种情况下, 没有交易完成, 所以最大利润为 0。
</pre>


## 解法：


从第一天开始累积收益，收益小于 0 时，说明在此之前都不能买。收益大于 0 时，和当前的最大收益比较，保存较大的。


```python
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        profit = 0
        
        for i in range(1, len(prices)):
            profit += prices[i] - prices[i-1]
            if profit < 0:
                profit = 0
            else:
                max_profit = max(max_profit, profit)
            
        return max_profit
```

另外一个思路，不断更新当前日期之前的最小值，作为买入价格，然后和当天的价格做差，就是当前卖出的收益，不断更新最大收益。（这个方法很棒）

```python
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        min_price = float('inf')
        
        for price in prices:
            min_price = min(price, min_price)
            max_profit = max(max_profit, price - min_price)
            
        return max_profit
```
