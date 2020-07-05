---
title: 二叉树的最大深度
qid: 104
tags: [树,深度优先搜索]
---


- 难度： 简单
- 通过率： 58.2%
- 题目链接：[https://leetcode.com/problems/maximum-depth-of-binary-tree](https://leetcode.com/problems/maximum-depth-of-binary-tree)


## 题目描述

来源于 [https://leetcode-cn.com/](https://leetcode-cn.com/)

<p>给定一个二叉树，找出其最大深度。</p>

<p>二叉树的深度为根节点到最远叶子节点的最长路径上的节点数。</p>

<p><strong>说明:</strong>&nbsp;叶子节点是指没有子节点的节点。</p>

<p><strong>示例：</strong><br>
给定二叉树 <code>[3,9,20,null,null,15,7]</code>，</p>

<pre>    3
   / \
  9  20
    /  \
   15   7</pre>

<p>返回它的最大深度&nbsp;3 。</p>


## 解法：

2019-8-2 21:26:01


解法一：层次遍历

```python

class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        max_depth = 0
        queue = [(root, 1)]
        
        while queue:
            node, depth = queue.pop(0)
            
            if not node:
                continue
                
            queue.append((node.left, depth + 1))
            queue.append((node.right, depth + 1))

            if max_depth < depth:
                max_depth = depth
            
        return max_depth
```

解法二：深度优先遍历

整个树的最大深度为左右子树的最大深度加 1 ，有了这样的理论基础，就不难写下如下递归解法。

```python
class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        if root:
            return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))
        else:
            return 0
```