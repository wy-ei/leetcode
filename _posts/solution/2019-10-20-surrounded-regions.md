---
title: 被围绕的区域
qid: 130
tags: [深度优先搜索,广度优先搜索,并查集]
---


- 难度： 中等
- 通过率： 21.6%
- 题目链接：[https://leetcode.com/problems/surrounded-regions](https://leetcode.com/problems/surrounded-regions)


## 题目描述

来源于 [https://leetcode-cn.com/](https://leetcode-cn.com/)

<p>给定一个二维的矩阵，包含&nbsp;<code>&#39;X&#39;</code>&nbsp;和&nbsp;<code>&#39;O&#39;</code>（<strong>字母 O</strong>）。</p>

<p>找到所有被 <code>&#39;X&#39;</code> 围绕的区域，并将这些区域里所有的&nbsp;<code>&#39;O&#39;</code> 用 <code>&#39;X&#39;</code> 填充。</p>

<p><strong>示例:</strong></p>

<pre>X X X X
X O O X
X X O X
X O X X
</pre>

<p>运行你的函数后，矩阵变为：</p>

<pre>X X X X
X X X X
X X X X
X O X X
</pre>

<p><strong>解释:</strong></p>

<p>被围绕的区间不会存在于边界上，换句话说，任何边界上的&nbsp;<code>&#39;O&#39;</code>&nbsp;都不会被填充为&nbsp;<code>&#39;X&#39;</code>。 任何不在边界上，或不与边界上的&nbsp;<code>&#39;O&#39;</code>&nbsp;相连的&nbsp;<code>&#39;O&#39;</code>&nbsp;最终都会被填充为&nbsp;<code>&#39;X&#39;</code>。如果两个元素在水平或垂直方向相邻，则称它们是&ldquo;相连&rdquo;的。</p>


## 解法：

先从四个边缘做深度优先搜索，把与边缘上的 `O` 相连的坐标都记录下来。然后对整个 board 遍历，将其中不与边缘上的 `O` 相连的 `O` 修改为 `X`。


```python
class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        if not board:
            return
        
        n_row = len(board)        
        n_col = len(board[0])
        seen = set()
        
        for i in range(n_row):
            self.mark(i, 0, board, seen)
            self.mark(i, n_col-1, board, seen)
            
        for i in range(n_col):
            self.mark(0, i, board, seen)
            self.mark(n_row-1, i, board, seen)
            
        for i_row in range(n_row):
            for i_col in range(n_col):
                if board[i_row][i_col] == 'O' and (i_row, i_col) not in seen:
                    board[i_row][i_col] = 'X'
        
            
    def mark(self, i_row, i_col, board, seen):
        if (i_row, i_col) in seen:
            return
        
        n_row = len(board)
        n_col = len(board[0])
        
        
        if i_row < 0 or i_row >= n_row:
            return
        
        if i_col < 0 or i_col >= n_col:
            return
        
        if board[i_row][i_col] == 'X':
            return
        
        
        seen.add((i_row, i_col))
        
        self.mark(i_row-1, i_col, board, seen)
        self.mark(i_row+1, i_col, board, seen)
        self.mark(i_row, i_col-1, board, seen)
        self.mark(i_row, i_col+1, board, seen)
```