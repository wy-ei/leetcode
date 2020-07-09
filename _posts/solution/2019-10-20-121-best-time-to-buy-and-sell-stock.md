---
title: 买卖股票的最佳时机
qid: 121
tags: [数组,动态规划]
---


- 难度： 简单
- 通过率： 45.4%
- 题目链接：[https://leetcode-cn.com/problems/best-time-to-buy-and-sell-stock](https://leetcode-cn.com/problems/best-time-to-buy-and-sell-stock)


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

计算出每日价格与前一日比较的涨幅，把问题转化为求子序列中的最大和的问题。

```c++
class Solution {
public:
    int maxProfit(vector<int>& prices) {
        if(prices.empty()){
            return 0;
        }
        int max_profit = 0;
        int profit = 0;
        for(int i=1;i<prices.size();i++){
            profit += prices[i] - prices[i-1];
            max_profit = max(max_profit, profit);
            profit = max(0, profit);
        }
        return max_profit;
    }
};
```

股票想要赚钱，那就是低买高卖。因此只需要记录下出现过的最低价格即可。

```c++
class Solution {
public:
    int maxProfit(vector<int>& prices) {
        if(prices.empty()){
            return 0;
        }
        int max_profit = 0;
        int lowest_price = prices[0];
        for(int i=1;i<prices.size();i++){
            max_profit = max(max_profit, prices[i] - lowest_price);
            lowest_price = min(prices[i], lowest_price);
        }
        return max_profit;
    }
};
```