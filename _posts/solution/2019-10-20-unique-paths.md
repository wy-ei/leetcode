---
title: 不同路径
qid: 62
tags: [数组,动态规划]
---


- 难度： 中等
- 通过率： 45.5%
- 题目链接：[https://leetcode.com/problems/unique-paths](https://leetcode.com/problems/unique-paths)


## 题目描述

来源于 [https://leetcode-cn.com/](https://leetcode-cn.com/)

<p>一个机器人位于一个 <em>m x n </em>网格的左上角 （起始点在下图中标记为&ldquo;Start&rdquo; ）。</p>

<p>机器人每次只能向下或者向右移动一步。机器人试图达到网格的右下角（在下图中标记为&ldquo;Finish&rdquo;）。</p>

<p>问总共有多少条不同的路径？</p>

<p><img src="https://assets.leetcode-cn.com/aliyun-lc-upload/uploads/2018/10/22/robot_maze.png"></p>

<p><small>例如，上图是一个7 x 3 的网格。有多少可能的路径？</small></p>

<p><strong>说明：</strong><em>m</em>&nbsp;和 <em>n </em>的值均不超过 100。</p>

<p><strong>示例&nbsp;1:</strong></p>

<pre><strong>输入:</strong> m = 3, n = 2
<strong>输出:</strong> 3
<strong>解释:</strong>
从左上角开始，总共有 3 条路径可以到达右下角。
1. 向右 -&gt; 向右 -&gt; 向下
2. 向右 -&gt; 向下 -&gt; 向右
3. 向下 -&gt; 向右 -&gt; 向右
</pre>

<p><strong>示例&nbsp;2:</strong></p>

<pre><strong>输入:</strong> m = 7, n = 3
<strong>输出:</strong> 28</pre>


## 解法 1 - 动态规划：

本题可用动态规划来做，用数组 m 来保存各个位置到右下角的路线数量。从右下角向左上角遍历，各个位置到右下角的路线数量为：

```
m[i][j] = m[i+1][j] + m[i][j+1]
```

在遍历中考虑一下边界即可。

```python
from collections import defaultdict

class Solution:
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        
        dp = defaultdict(int)
        dp[(m-1,n-1)] = 1
        
        for col in range(n-1, -1, -1):
            for row in range(m-1, -1, -1):
                if row < m-1:
                    dp[(row, col)] += dp[(row+1, col)]
                
                if col < n-1:
                    dp[(row, col)] += dp[(row, col+1)]
        
        return dp[(0,0)]
```

## 解法 2 - 排列组合

另外，从左上角走到右下角一个需要走 m+n-2 步，其中向下走 m-1 步，向右走 n-1 步，因此一共有 `C(m+n-1,m-1)` 中路线。

```python
# C(n, k)
def comb(self, n, k):
    m = n + 1
    nterms = min(k, n - k)

    numerator = 1
    denominator = 1
    for j in range(1, nterms + 1):
        numerator *= m - j
        denominator *= j

    return numerator // denominator

class Solution:
    def uniquePaths(self, m, n):
        return comb(m+n-2, n-1)
```