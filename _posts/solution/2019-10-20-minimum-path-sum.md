---
title: 最小路径和
qid: 64
tags: [数组,动态规划]
---


- 难度： 中等
- 通过率： 44.5%
- 题目链接：[https://leetcode.com/problems/minimum-path-sum](https://leetcode.com/problems/minimum-path-sum)


## 题目描述

来源于 [https://leetcode-cn.com/](https://leetcode-cn.com/)

<p>给定一个包含非负整数的 <em>m</em>&nbsp;x&nbsp;<em>n</em>&nbsp;网格，请找出一条从左上角到右下角的路径，使得路径上的数字总和为最小。</p>

<p><strong>说明：</strong>每次只能向下或者向右移动一步。</p>

<p><strong>示例:</strong></p>

<pre><strong>输入:</strong>
[
&nbsp; [1,3,1],
  [1,5,1],
  [4,2,1]
]
<strong>输出:</strong> 7
<strong>解释:</strong> 因为路径 1&rarr;3&rarr;1&rarr;1&rarr;1 的总和最小。
</pre>


## 解法：

```python
class Solution:
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        m = len(grid)
        n = len(grid[0])
        
        inf = float('inf')
        
        for col in range(n-1, -1, -1):
            for row in range(m-1, -1, -1):
                if row < m-1:
                    down = grid[row+1][col]
                else:
                    down = inf
                    
                if col < n-1:
                    right = grid[row][col+1]
                else:
                    right = inf
                
                if down != inf or right != inf:
                    grid[row][col] += min(right, down)
            
        return grid[0][0]
```