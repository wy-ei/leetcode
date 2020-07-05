---
title: 二叉树的锯齿形层次遍历
qid: 103
tags: [栈,树,广度优先搜索]
---


- 难度： 中等
- 通过率： 39.6%
- 题目链接：[https://leetcode.com/problems/binary-tree-zigzag-level-order-traversal](https://leetcode.com/problems/binary-tree-zigzag-level-order-traversal)


## 题目描述

来源于 [https://leetcode-cn.com/](https://leetcode-cn.com/)

<p>给定一个二叉树，返回其节点值的锯齿形层次遍历。（即先从左往右，再从右往左进行下一层遍历，以此类推，层与层之间交替进行）。</p>

<p>例如：<br>
给定二叉树&nbsp;<code>[3,9,20,null,null,15,7]</code>,</p>

<pre>    3
   / \
  9  20
    /  \
   15   7
</pre>

<p>返回锯齿形层次遍历如下：</p>

<pre>[
  [3],
  [20,9],
  [15,7]
]
</pre>


## 解法：

先进行层次遍历，然后根据层数来翻转。也可以在遍历的过程中，根据层数决定在头部或是尾部插入。但我觉得多次在头部插入，效率不如最后进行翻转。


```python
from collections import deque

class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        queue = deque()
        result = []

        if root:
            queue.append((root, 0))

        while len(queue):
            node, depth = queue.popleft()

            if len(result) == depth:
                result.append([])

            result[depth].append(node.val)

            if node.left:
                queue.append((node.left, depth + 1))
            if node.right:
                queue.append((node.right, depth + 1))

        for depth, items in enumerate(result):
            if depth % 2 == 1:
                items.reverse()

        return result
```