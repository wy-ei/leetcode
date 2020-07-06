---
title: 二叉树的最小深度
qid: 111
tags: [树,深度优先搜索,广度优先搜索]
---


- 难度： 简单
- 通过率： 34.5%
- 题目链接：[https://leetcode-cn.com/problems/minimum-depth-of-binary-tree](https://leetcode-cn.com/problems/minimum-depth-of-binary-tree)


## 题目描述

来源于 [https://leetcode-cn.com/](https://leetcode-cn.com/)

<p>给定一个二叉树，找出其最小深度。</p>

<p>最小深度是从根节点到最近叶子节点的最短路径上的节点数量。</p>

<p><strong>说明:</strong>&nbsp;叶子节点是指没有子节点的节点。</p>

<p><strong>示例:</strong></p>

<p>给定二叉树&nbsp;<code>[3,9,20,null,null,15,7]</code>,</p>

<pre>    3
   / \
  9  20
    /  \
   15   7</pre>

<p>返回它的最小深度 &nbsp;2.</p>


## 解法：

层次遍历，遇到第一个没有左右孩子的节点时停止。

```python
class Solution:
    def minDepth(self, root):
        if not root:
            return 0
        
        queue = [(root, 1)]
        
        while queue:
            node, depth = queue.pop(0)
            if not (node.left or node.right):
                return depth
            
            depth += 1
            if node.left:
                queue.append((node.left, depth))
            if node.right:
                queue.append((node.right, depth))
```