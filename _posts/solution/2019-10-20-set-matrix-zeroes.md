---
title: 矩阵置零
qid: 73
tags: [数组]
---


- 难度： 中等
- 通过率： 38.4%
- 题目链接：[https://leetcode-cn.com/problems/set-matrix-zeroes](https://leetcode-cn.com/problems/set-matrix-zeroes)


## 题目描述

来源于 [https://leetcode-cn.com/](https://leetcode-cn.com/)

<p>给定一个&nbsp;<em>m</em> x <em>n</em> 的矩阵，如果一个元素为 0，则将其所在行和列的所有元素都设为 0。请使用<strong><a href="http://baike.baidu.com/item/%E5%8E%9F%E5%9C%B0%E7%AE%97%E6%B3%95" target="_blank">原地</a></strong>算法<strong>。</strong></p>

<p><strong>示例&nbsp;1:</strong></p>

<pre><strong>输入:</strong> 
[
&nbsp; [1,1,1],
&nbsp; [1,0,1],
&nbsp; [1,1,1]
]
<strong>输出:</strong> 
[
&nbsp; [1,0,1],
&nbsp; [0,0,0],
&nbsp; [1,0,1]
]
</pre>

<p><strong>示例&nbsp;2:</strong></p>

<pre><strong>输入:</strong> 
[
&nbsp; [0,1,2,0],
&nbsp; [3,4,5,2],
&nbsp; [1,3,1,5]
]
<strong>输出:</strong> 
[
&nbsp; [0,0,0,0],
&nbsp; [0,4,5,0],
&nbsp; [0,3,1,0]
]</pre>

<p><strong>进阶:</strong></p>

<ul>
	<li>一个直接的解决方案是使用 &nbsp;O(<em>m</em><em>n</em>)&nbsp;的额外空间，但这并不是一个好的解决方案。</li>
	<li>一个简单的改进方案是使用 O(<em>m</em>&nbsp;+&nbsp;<em>n</em>) 的额外空间，但这仍然不是最好的解决方案。</li>
	<li>你能想出一个常数空间的解决方案吗？</li>
</ul>


## 解法：

## 解法 1：m+n 空间

使用两个 set 记录下含有 0 的行和含有 0 的列，然后遍历这两个 set 将相应的行和列置为 0。这是最直接的想法。

```python
class Solution:
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        m = len(matrix)
        n = len(matrix[0])
        
        zero_row_set = set()
        zero_col_set = set()
        
        for row in range(m):
            for col in range(n):
                if matrix[row][col] == 0:
                    zero_row_set |= {row}
                    zero_col_set |= {col}
        
        for row in zero_row_set:
            for col in range(n):
                matrix[row][col] = 0
        
        for col in zero_col_set:
            for row in range(m):
                matrix[row][col] = 0
```

## 解法 2：不使用额外空间

在 leetcode 上看了一下[大佬的解答](https://leetcode-cn.com/problems/set-matrix-zeroes/discuss/26014/Any-shorter-O(1)-space-solution)，我咋没想到哩。

使用 matrix 的第一行来记录各列中是否有 0，使用 matrix 的第一列记录各行中是否含有 0。

如果 `matrix[i][j] == 0`，那么第 `i` 行会被置零，因此设置 `matrix[i][0] = 0` 并没有副作用，同样的第 `j` 列会被置零，因此设置 `matrix[0][j] = 0` 也无副作用。

因为 `matrix[0][0]` 既要记录第 1 列的信息，也要记录第 1 行的信息，这显然冲突了，因此需要定义一个变量，专门用来记录第一列中是否有 0，而使用 `matrix[0][0]` 来记录第一行中是否有 0。

第一次扫描先把含零的信息记录下来，第二次由最后一行向上遍历，利用第一行行第一列中记录的信息，来把相应的行列置零。

实现代码如下：

```python
class Solution:
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        m = len(matrix)
        n = len(matrix[0])
        
        col_0_has_0 = False
        
        for row in range(m):
            if matrix[row][0] == 0:
                col_0_has_0 = True
            for col in range(1, n):
                if matrix[row][col] == 0:
                    matrix[row][0] = 0
                    matrix[0][col] = 0
        
        for row in range(m-1, -1, -1):
            for col in range(n-1, 0, -1):
                if matrix[0][col] == 0 or matrix[row][0] == 0:
                    matrix[row][col] = 0
            
            if col_0_has_0:
                matrix[row][0] = 0
```
