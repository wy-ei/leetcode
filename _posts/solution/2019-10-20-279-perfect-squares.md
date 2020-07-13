---
title: 完全平方数
qid: 279
tag: [深度优先搜索, 数学, 动态规划]
---

- 难度： 中等
- 通过率： 39.6%
- 题目链接：[https://leetcode-cn.com/problems/perfect-squares](https://leetcode-cn.com/problems/perfect-squares)


## 题目描述

来源于 [https://leetcode-cn.com/](https://leetcode-cn.com/)

<p>给定正整数&nbsp;<em>n</em>，找到若干个完全平方数（比如&nbsp;<code>1, 4, 9, 16, ...</code>）使得它们的和等于<em> n</em>。你需要让组成和的完全平方数的个数最少。</p>

<p><strong>示例&nbsp;1:</strong></p>

<pre><strong>输入:</strong> <em>n</em> = <code>12</code>
<strong>输出:</strong> 3 
<strong>解释: </strong><code>12 = 4 + 4 + 4.</code></pre>

<p><strong>示例 2:</strong></p>

<pre><strong>输入:</strong> <em>n</em> = <code>13</code>
<strong>输出:</strong> 2
<strong>解释: </strong><code>13 = 4 + 9.</code></pre>


## 解法：

典型的深度优先搜索问题，给定正整数 n，然后令 `i = sqrt(n) 到 1`，从 n 中减去 `i*i`，余下的数再次做同样的操作，直到余下的数为 0 为止。

下面 `dfs` 中第二个参数 `m`，记录了上次从 n 中减去的 i*i 对应的 i 的值。下次减去的内容一定要小于等于这个数，这是剪枝策略。因为 `10 = 3*3 + 1*1` 而且 `10 = 1*1 + 3*3`。

```c++
class Solution {
public:
    int numSquares(int n) {
        int min_len = INT_MAX;
        dfs(n, INT_MAX, 0, min_len);
        return min_len;
    }
    void dfs(int n, int m, int len, int& min_len){
        if(n == 0){
            min_len = len;
            return;
        }
        if(n < 0 || len >= min_len){
            return;
        }
        m = min(m, static_cast<int>(sqrt(n)));
        for(int i=m;i>0;i--){
            dfs(n - i*i, i, len+1, min_len);
        }
    }
};
```