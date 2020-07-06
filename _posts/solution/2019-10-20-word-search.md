---
title: 单词搜索
qid: 79
tags: [数组,回溯算法]
---


- 难度： 中等
- 通过率： 29.8%
- 题目链接：[https://leetcode-cn.com/problems/word-search](https://leetcode-cn.com/problems/word-search)


## 题目描述

来源于 [https://leetcode-cn.com/](https://leetcode-cn.com/)

<p>给定一个二维网格和一个单词，找出该单词是否存在于网格中。</p>

<p>单词必须按照字母顺序，通过相邻的单元格内的字母构成，其中&ldquo;相邻&rdquo;单元格是那些水平相邻或垂直相邻的单元格。同一个单元格内的字母不允许被重复使用。</p>

<p><strong>示例:</strong></p>

<pre>board =
[
  [&#39;A&#39;,&#39;B&#39;,&#39;C&#39;,&#39;E&#39;],
  [&#39;S&#39;,&#39;F&#39;,&#39;C&#39;,&#39;S&#39;],
  [&#39;A&#39;,&#39;D&#39;,&#39;E&#39;,&#39;E&#39;]
]

给定 word = &quot;<strong>ABCCED</strong>&quot;, 返回 <strong>true</strong>.
给定 word = &quot;<strong>SEE</strong>&quot;, 返回 <strong>true</strong>.
给定 word = &quot;<strong>ABCB</strong>&quot;, 返回 <strong>false</strong>.</pre>


## 解法：

从各个位置进行深度优先搜索，将访问过位置设置为特殊字符，防止重复访问。在退出时恢复为原字符。

```python
class Solution:
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """

        for x in range(len(board)):
            for y in range(len(board[0])):
                if self.__exist(board, word, 0, x, y) == True:
                    return True

        return False

    def __exist(self, board, word, i, x, y):
        if i == len(word):
            return True

        if x < 0 or x >= len(board) or y < 0 or y >= len(board[0]):
            return False

        if board[x][y] != word[i]:
            return False

        t = board[x][y]
        board[x][y] = "_#_" # arbitrary special str
        exist = (
            self.__exist(board, word, i + 1, x - 1, y)
            or self.__exist(board, word, i + 1, x + 1, y)
            or self.__exist(board, word, i + 1, x, y - 1)
            or self.__exist(board, word, i + 1, x, y + 1)
        )
        board[x][y] = t
        return exist
```