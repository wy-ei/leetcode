---
title: 有效的数独
qid: 36
tags: [哈希表]
---


- 难度： 中等
- 通过率： 40.9%
- 题目链接：[https://leetcode-cn.com/problems/valid-sudoku](https://leetcode-cn.com/problems/valid-sudoku)


## 题目描述

来源于 [https://leetcode-cn.com/](https://leetcode-cn.com/)

<p>判断一个&nbsp;9x9 的数独是否有效。只需要<strong>根据以下规则</strong>，验证已经填入的数字是否有效即可。</p>

<ol>
	<li>数字&nbsp;<code>1-9</code>&nbsp;在每一行只能出现一次。</li>
	<li>数字&nbsp;<code>1-9</code>&nbsp;在每一列只能出现一次。</li>
	<li>数字&nbsp;<code>1-9</code>&nbsp;在每一个以粗实线分隔的&nbsp;<code>3x3</code>&nbsp;宫内只能出现一次。</li>
</ol>

<p><img src="https://upload.wikimedia.org/wikipedia/commons/thumb/f/ff/Sudoku-by-L2G-20050714.svg/250px-Sudoku-by-L2G-20050714.svg.png" style="height: 250px; width: 250px;"></p>

<p><small>上图是一个部分填充的有效的数独。</small></p>

<p>数独部分空格内已填入了数字，空白格用&nbsp;<code>&#39;.&#39;</code>&nbsp;表示。</p>


## 解法：

这个题就是简单地检查各行各列以及各个子块中有没有重复的数字出现。

可能最麻烦的是寻找判断 `3*3` 小方块中是否有重复元素了，这里采取的思路是通过外层循环的 `i` 定位方块左上角，然后使用内循环的 `j` 定位方块中各个单元。这样可以保证外层循环每循环一次，能够检查一行、一列、一个 `3*3` 方块。

```python
def isValidSudoku(board):
    """
    :type board: List[List[str]]
    :rtype: bool
    """
    for i in range(9):
        row_set = set()
        col_set = set()
        box_set = set()

        # 3*3 小块的左上角坐标
        box_x = i // 3 * 3
        box_y = (i % 3) * 3

        for j in range(9):

            # check row
            num = board[i][j]
            if num != '.' and num in row_set:
                return False
            else:
                row_set.add(num)


            # check column
            num = board[j][i]
            if num != '.' and num in col_set:
                return False
            else:
                col_set.add(num)

            # check subbox
            
            # 3*3 小方块中各个单元相对于左上角的偏移量
            cell_x = j // 3
            cell_y = j % 3
            num = board[box_x + cell_x][box_y + cell_y]
            if num != '.' and num in box_set:
                return False
            else:
                box_set.add(num)


    return True
```