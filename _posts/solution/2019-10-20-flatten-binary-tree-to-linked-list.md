---
title: 二叉树展开为链表
qid: 114
tags: [树,深度优先搜索]
---


- 难度： 中等
- 通过率： 40.2%
- 题目链接：[https://leetcode-cn.com/problems/flatten-binary-tree-to-linked-list](https://leetcode-cn.com/problems/flatten-binary-tree-to-linked-list)


## 题目描述

来源于 [https://leetcode-cn.com/](https://leetcode-cn.com/)

<p>给定一个二叉树，<a href="https://baike.baidu.com/item/%E5%8E%9F%E5%9C%B0%E7%AE%97%E6%B3%95/8010757" target="_blank">原地</a>将它展开为链表。</p>

<p>例如，给定二叉树</p>

<pre>    1
   / \
  2   5
 / \   \
3   4   6</pre>

<p>将其展开为：</p>

<pre>1
 \
  2
   \
    3
     \
      4
       \
        5
         \
          6</pre>


## 解法：

先序遍历，始终记录下前一个节点，然后将当前节点接在前一个节点的右孩子上。

为了避免初始阶段 last 为空（即开始的时候**前一个节点**是不存在的），可以随意给 last 初始化一个节点，这并不影响结果。

```python
class Solution:
    def flatten(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        
        stack = [root]
        last = TreeNode(0)
        
        while stack:
            node = stack.pop()
            if not node:
                continue
        
            last.right = node
            last = node

            stack.append(node.right)
            stack.append(node.left)
            node.left = None
```