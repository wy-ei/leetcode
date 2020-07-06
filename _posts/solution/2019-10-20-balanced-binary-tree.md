---
title: 平衡二叉树
qid: 110
tags: [树,深度优先搜索]
---


- 难度： 简单
- 通过率： 39.9%
- 题目链接：[https://leetcode-cn.com/problems/balanced-binary-tree](https://leetcode-cn.com/problems/balanced-binary-tree)


## 题目描述

来源于 [https://leetcode-cn.com/](https://leetcode-cn.com/)

<p>给定一个二叉树，判断它是否是高度平衡的二叉树。</p>

<p>本题中，一棵高度平衡二叉树定义为：</p>

<blockquote>
<p>一个二叉树<em>每个节点&nbsp;</em>的左右两个子树的高度差的绝对值不超过1。</p>
</blockquote>

<p><strong>示例 1:</strong></p>

<p>给定二叉树 <code>[3,9,20,null,null,15,7]</code></p>

<pre>    3
   / \
  9  20
    /  \
   15   7</pre>

<p>返回 <code>true</code> 。<br>
<br>
<strong>示例 2:</strong></p>

<p>给定二叉树 <code>[1,2,2,3,3,null,null,4,4]</code></p>

<pre>       1
      / \
     2   2
    / \
   3   3
  / \
 4   4
</pre>

<p>返回&nbsp;<code>false</code> 。</p>


## 解法：

这个问题可以递归地去检查子树的是否平衡，深度的计算应该是从树的叶子开始，然后复用子树的求得的深度。看到一些解法，直接去求子树的深度，但是没有复用深度，造成了很多没必要的计算。

这里一个困难点在于，如何在计算深度的同时，向外层传递不平衡的信息，以便在发现不平衡时，算法可以立刻停止。这里我使用了异常机制，在出现不平衡后断言不成立，会抛出异常。

```python
class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        try:
            self.check_balance(root)
        except:
            return False
        
        return True
    
    def check_balance(self, node):
        if not node:
            return 0
        
        left_height = self.check_balance(node.left)
        right_height = self.check_balance(node.right)
        
        assert abs(left_height - right_height) <= 1, 'unblance'
        
        return 1 + max(left_height, right_height)
```

后来，又看到了下面这种解法，相当精妙。代码非常干净，没有一点拖泥带水。`blance` 函数中发现不平衡后，就返回 -1，随后整个递归过程就全部退出了。

```python
class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        return self.blance(root) != -1
    
    def blance(self, node):
        if not node:
            return 0
        
        lh = self.blance(node.left)
        if lh == -1:
            return -1
        
        rh = self.blance(node.right)
        if rh == -1:
            return -1
        
        if abs(lh - rh) > 1:
            return -1
        
        return 1 + max(lh, rh)
```