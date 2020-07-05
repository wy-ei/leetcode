---
title: 二叉树的层序遍历
qid: 102
tags: [树,广度优先搜索]
---


- 难度： 中等
- 通过率： 46.1%
- 题目链接：[https://leetcode.com/problems/binary-tree-level-order-traversal](https://leetcode.com/problems/binary-tree-level-order-traversal)


## 题目描述

来源于 [https://leetcode-cn.com/](https://leetcode-cn.com/)

<p>给定一个二叉树，返回其按层次遍历的节点值。 （即逐层地，从左到右访问所有节点）。</p>

<p>例如:<br>
给定二叉树:&nbsp;<code>[3,9,20,null,null,15,7]</code>,</p>

<pre>    3
   / \
  9  20
    /  \
   15   7
</pre>

<p>返回其层次遍历结果：</p>

<pre>[
  [3],
  [9,20],
  [15,7]
]
</pre>


## 解法：

层次遍历的常规操作。维护一个队列，从根节点开始遍历二叉树，遇到一个节点后就将其放入队列，下次遍历的节点，从队列的头部取。这样得到的效果就是，先入队的先被访问，即先访问第一层，而后第二层，以此类推。最终就实现了层次遍历。

此处队列中保存了节点和层数，以实现将不同层的节点的值放到相应的数组中。

```python
# 2019-8-2 21:13:04

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        queue = []
        result = []
        
        if root:
            queue.append((root, 0))
            
        while queue:
            node, level = queue.pop(0)
            
            if len(result) < level + 1:
                result.append([])
            
            result[level].append(node.val)
            
            if node.left:
                queue.append((node.left, level + 1))
            if node.right:
                queue.append((node.right, level + 1))

        return result
```

上面的方法，在出队的时候一次出一个节点，为了区别节点的层级，额外加入了 depth 信息。其实没有必要。可以一次性把同一层的节点全部出队并处理。

```python
class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        queue = []
        result = []
        
        if root:
            queue.append(root)

        while queue:
            values = []
            for _ in range(len(queue)):
                node = queue.pop(0)
                values.append(node.val)

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            result.append(values)            

        return result
```