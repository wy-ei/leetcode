---
title: 零钱兑换
qid: 322
tags: [动态规划]
---


- 难度： 中等
- 通过率： 28.1%
- 题目链接：[https://leetcode.com/problems/coin-change](https://leetcode.com/problems/coin-change)


## 题目描述

来源于 [https://leetcode-cn.com/](https://leetcode-cn.com/)

<p>给定不同面额的硬币 coins 和一个总金额 amount。编写一个函数来计算可以凑成总金额所需的最少的硬币个数。如果没有任何一种硬币组合能组成总金额，返回&nbsp;<code>-1</code>。</p>

<p><strong>示例&nbsp;1:</strong></p>

<pre><strong>输入: </strong>coins = <code>[1, 2, 5]</code>, amount = <code>11</code>
<strong>输出: </strong><code>3</code> 
<strong>解释:</strong> 11 = 5 + 5 + 1</pre>

<p><strong>示例 2:</strong></p>

<pre><strong>输入: </strong>coins = <code>[2]</code>, amount = <code>3</code>
<strong>输出: </strong>-1</pre>

<p><strong>说明</strong>:<br>
你可以认为每种硬币的数量是无限的。</p>


## 解法：

```python
class Solution:
    def coinChange(self, coins, amount):
        inf = float('inf')
        dp = [0] + [inf] * amount
        
        for i in range(1, amount+1):
            for coin in coins:
                if i >= coin and dp[i-coin] != inf:
                    dp[i] = min(dp[i-coin]+1, dp[i])
                    
        if dp[amount] == inf: dp[amount] = -1
            
        return dp[amount]
```