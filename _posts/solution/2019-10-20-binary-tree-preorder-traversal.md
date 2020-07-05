---
title: 二叉树的前序遍历
qid: 144
tags: [栈,树]
---


- 难度： 中等
- 通过率： 49.5%
- 题目链接：[https://leetcode.com/problems/binary-tree-preorder-traversal](https://leetcode.com/problems/binary-tree-preorder-traversal)


## 题目描述

来源于 [https://leetcode-cn.com/](https://leetcode-cn.com/)

<p>给定一个二叉树，返回它的&nbsp;<em>前序&nbsp;</em>遍历。</p>

<p>&nbsp;<strong>示例:</strong></p>

<pre><strong>输入:</strong> [1,null,2,3]  
   1
    \
     2
    /
   3 

<strong>输出:</strong> [1,2,3]
</pre>

<p><strong>进阶:</strong>&nbsp;递归算法很简单，你可以通过迭代算法完成吗？</p>


## 解法：

**递归实现**

```python
class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        
        if not root:
            return []
        
        result = [root.val]        
        result += self.preorderTraversal(root.left)
        result += self.preorderTraversal(root.right)
        
        return result
```

**基于栈的实现**

```python
class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        stack, result = [], []

        if root:
            stack.append(root)

        while stack:
            node = stack.pop()
            result.append(node.val)
            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)

        return result
```

2019-8-3 19:41:45