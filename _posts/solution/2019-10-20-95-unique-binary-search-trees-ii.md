---
title: 不同的二叉搜索树 II
qid: 95
tags: [树,动态规划]
---


- 难度： 中等
- 通过率： 34.2%
- 题目链接：[https://leetcode-cn.com/problems/unique-binary-search-trees-ii](https://leetcode-cn.com/problems/unique-binary-search-trees-ii)


## 题目描述

来源于 [https://leetcode-cn.com/](https://leetcode-cn.com/)

<p>给定一个整数 <em>n</em>，生成所有由 1 ...&nbsp;<em>n</em> 为节点所组成的<strong>二叉搜索树</strong>。</p>

<p><strong>示例:</strong></p>

<pre><strong>输入:</strong> 3
<strong>输出:</strong>
[
&nbsp; [1,null,3,2],
&nbsp; [3,2,null,1],
&nbsp; [3,1,null,null,2],
&nbsp; [2,1,3],
&nbsp; [1,null,2,null,3]
]
<strong>解释:</strong>
以上的输出对应以下 5 种不同结构的二叉搜索树：

   1         3     3      2      1
    \       /     /      / \      \
     3     2     1      1   3      2
    /     /       \                 \
   2     1         2                 3
</pre>


## 解法：

把序列从某个位置切分，切分点为根节点，左右两边的分别用来构造左右子树。因为左右子树的可能性会很多。构造的左右子树是两个列表。用根节点组合不同的左右子树，即可得到答案。

```python
import itertools

class Solution:
    def generateTrees(self, n: int) -> List[TreeNode]:
        if n == 0:
            return []
        return self._generate_trees(1, n)
    
    def _generate_trees(self, lo, hi):
        trees = []

        if lo > hi:
            trees.append(None)
        
        for i in range(lo, hi+1):
            left_trees = self._generate_trees(lo, i-1)
            right_trees = self._generate_trees(i+1, hi)
            for left, right in itertools.product(left_trees, right_trees):
                node = TreeNode(i)
                node.left = left
                node.right = right
                trees.append(node)
        return trees
```