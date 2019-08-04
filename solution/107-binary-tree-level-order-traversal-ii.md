## 107. Binary Tree Level Order Traversal II

- 难度： 简单
- 通过率： 44.9%
- 题目链接：[https://leetcode.com/problems/binary-tree-level-order-traversal-ii](https://leetcode.com/problems/binary-tree-level-order-traversal-ii)


## 题目描述

来源于 [https://leetcode-cn.com/](https://leetcode-cn.com/)

<p>给定一个二叉树，返回其节点值自底向上的层次遍历。 （即按从叶子节点所在层到根节点所在的层，逐层从左向右遍历）</p>

<p>例如：<br>
给定二叉树 <code>[3,9,20,null,null,15,7]</code>,</p>

<pre>    3
   / \
  9  20
    /  \
   15   7
</pre>

<p>返回其自底向上的层次遍历为：</p>

<pre>[
  [15,7],
  [9,20],
  [3]
]
</pre>


## 解法：

提到二叉树的层次遍历，就会想到使用队列。常见的做法是在 `while` 主循环中，一次出队一个节点，并处理该节点。本题中需要将同一层级的节点的值放在一个数组中，所有最好能够一次性处理同一层的所有节点。

下面的代码中队列的概念已经没有了，在主循环中，一次性处理完全部的节点。在处理过程中把孩子节点收集起来。而后处理这些孩子节点，并得到新的孩子节点。直到没有了孩子节点，循环退出。

```python
class Solution:
    def levelOrderBottom(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []

        result = []
        children = []

        while children:
            values = []
            new_children = []
            for node in children:
                values.append(node.val)
                if node.left:
                    new_children.append(node.left)
                if node.right:
                    new_children.append(node.right)

            result.append(values)            
            children = new_children
            
        result.reverse()
        
        return result
```

如果非要使用上队列的概念，可以在主循环中，一次性把同一层的所有节点都出队。

```python
class Solution:
    def levelOrderBottom(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []

        result = []
        queue = [root]

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

        result.reverse()

        return result
```

2019-8-3 18:14:51