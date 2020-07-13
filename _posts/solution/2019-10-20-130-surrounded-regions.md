---
title: 被围绕的区域
qid: 130
tags: [深度优先搜索,广度优先搜索,并查集]
---


- 难度： 中等
- 通过率： 21.6%
- 题目链接：[https://leetcode-cn.com/problems/surrounded-regions](https://leetcode-cn.com/problems/surrounded-regions)


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

先从四个边缘做深度优先搜索，把与边缘上的 `O` 相连的位置标记为 `*`。然后对整个 `board` 遍历，把 `O` 设为 `X`，把 `*` 设为 `O`。


```python
class Solution:
    def solve(self, board) -> None:
        if not board:
            return

        n_row = len(board)
        n_col = len(board[0])

        for i in range(n_row):
            self.dfs(i, 0, board)
            self.dfs(i, n_col-1, board)

        for i in range(n_col):
            self.dfs(0, i, board)
            self.dfs(n_row-1, i, board)

        for row in range(n_row):
            for col in range(n_col):
                ch = board[row][col]
                if ch == 'O':
                    board[row][col] = 'X'
                if ch == '*':
                    board[row][col] = 'O'
                
    def dfs(self, row, col, board):
        n_row = len(board)
        n_col = len(board[0])

        if row < 0 or row >= n_row:
            return

        if col < 0 or col >= n_col:
            return

        ch = board[row][col]
        if ch == 'X' or ch == '*':
            return

        board[row][col] = '*'
        self.dfs(row-1, col, board)
        self.dfs(row+1, col, board)
        self.dfs(row, col-1, board)
        self.dfs(row, col+1, board)

```