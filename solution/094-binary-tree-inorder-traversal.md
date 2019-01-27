## 94. Binary Tree Inorder Traversal

- 难度： 中等
- 通过率： 53.9%
- 题目链接：[https://leetcode.com/problems/binary-tree-inorder-traversal](https://leetcode.com/problems/binary-tree-inorder-traversal)


## 题目描述

来源于 [https://leetcode-cn.com/](https://leetcode-cn.com/)

<p>给定一个二叉树，返回它的<em>中序&nbsp;</em>遍历。</p>

<p><strong>示例:</strong></p>

<pre><strong>输入:</strong> [1,null,2,3]
   1
    \
     2
    /
   3

<strong>输出:</strong> [1,3,2]</pre>

<p><strong>进阶:</strong>&nbsp;递归算法很简单，你可以通过迭代算法完成吗？</p>


## 解法：

中序变量，即按照 左->中->右 的次序来对二叉树进行遍历。对树进行遍历使用递归会非常简单。当然，不使用递归能够带来性能上的提升。

### 解法 1 - 递归

```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        result = []
        self.__inorderTraversal(root, result)
        return result
        
    def __inorderTraversal(self, node, result):
        if not node:
            return
        
        self.__inorderTraversal(node.left, result)
        result.append(node.val)
        self.__inorderTraversal(node.right, result)
```

### 解法 2 - 基于栈


```python
class Solution:
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        result = []
        stack = []
        node = root
        while stack or node:
            if node:
                stack.append(node)
                node = node.left
            else:
                node = stack.pop()
                result.append(node.val)
                node = node.right

        return result
```