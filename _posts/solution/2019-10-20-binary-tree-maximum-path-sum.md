---
title: 二叉树中的最大路径和
qid: 124
tags: [树,深度优先搜索]
---


- 难度： 困难
- 通过率： 28.8%
- 题目链接：[https://leetcode-cn.com/problems/binary-tree-maximum-path-sum](https://leetcode-cn.com/problems/binary-tree-maximum-path-sum)


## 题目描述

来源于 [https://leetcode-cn.com/](https://leetcode-cn.com/)

<p>给定一个<strong>非空</strong>二叉树，返回其最大路径和。</p>

<p>本题中，路径被定义为一条从树中任意节点出发，达到任意节点的序列。该路径<strong>至少包含一个</strong>节点，且不一定经过根节点。</p>

<p><strong>示例 1:</strong></p>

<pre><strong>输入:</strong> [1,2,3]

       <strong>1</strong>
      <strong>/ \</strong>
     <strong>2</strong>   <strong>3</strong>

<strong>输出:</strong> 6
</pre>

<p><strong>示例&nbsp;2:</strong></p>

<pre><strong>输入:</strong> [-10,9,20,null,null,15,7]

&nbsp;  -10
&nbsp; &nbsp;/ \
&nbsp; 9 &nbsp;<strong>20</strong>
&nbsp; &nbsp; <strong>/ &nbsp;\</strong>
&nbsp; &nbsp;<strong>15 &nbsp; 7</strong>

<strong>输出:</strong> 42</pre>


## 解法：

如果一个节点包含在最大和路径中, 有下面两种情况:

1. 该节点加上左右子树中路径和较大且大于 0 的那个子树（可能不存在），一起构成最大路径。
2. 该节点的左右子树都在最大路径中, 与该节点一起构成了最终的最大路径。

```
    10  <--- 第二种情况
   / \
  9  20 <--- 第一种情况
    /  \
   15   7
```

```python
class Solution:
    def maxPathSum(self, root: TreeNode) -> int:
        max_sum = float('-inf')
        
        def max_path_sum(node):
            nonlocal max_sum
            
            if not node:
                return 0

            max_left = max_path_sum(node.left)
            max_right = max_path_sum(node.right)
            
            max_child = max(max_left, max_right)
            sum_child = max_left + max_right
            
            max_sum = max(sum_child + node.val, max_sum)
            
            return max(max_child + node.val, 0)
        
        max_path_sum(root)
        
        return max_sum
```