---
title: 杨辉三角 II
qid: 119
tags: [数组]
---


- 难度： 简单
- 通过率： 41.1%
- 题目链接：[https://leetcode-cn.com/problems/pascals-triangle-ii](https://leetcode-cn.com/problems/pascals-triangle-ii)


## 题目描述

来源于 [https://leetcode-cn.com/](https://leetcode-cn.com/)

<p>给定一个非负索引&nbsp;<em>k</em>，其中 <em>k</em>&nbsp;&le;&nbsp;33，返回杨辉三角的第 <em>k </em>行。</p>

<p><img alt="" src="https://upload.wikimedia.org/wikipedia/commons/0/0d/PascalTriangleAnimated2.gif"></p>

<p><small>在杨辉三角中，每个数是它左上方和右上方的数的和。</small></p>

<p><strong>示例:</strong></p>

<pre><strong>输入:</strong> 3
<strong>输出:</strong> [1,3,3,1]
</pre>

<p><strong>进阶：</strong></p>

<p>你可以优化你的算法到 <em>O</em>(<em>k</em>) 空间复杂度吗？</p>


## 解法：

中规中矩的实现，不知道第 n 行的值，是不是有一个推导公式可以直接得出来，不过不想深究了。

```python
class Solution:
    def getRow(self, row_index: int) -> List[int]:
        row = [1] * (row_index + 1)
        
        for i_row in range(row_index):
            for i in range(i_row, 0, -1):
                row[i] = row[i-1] + row[i]

        return row
```

