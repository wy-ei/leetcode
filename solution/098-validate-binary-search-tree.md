## 98. Validate Binary Search Tree

- 难度： 中等
- 通过率： 24.9%
- 题目链接：[https://leetcode.com/problems/validate-binary-search-tree](https://leetcode.com/problems/validate-binary-search-tree)


## 题目描述

来源于 [https://leetcode-cn.com/](https://leetcode-cn.com/)

<p>给定一个二叉树，判断其是否是一个有效的二叉搜索树。</p>

<p>假设一个二叉搜索树具有如下特征：</p>

<ul>
	<li>节点的左子树只包含<strong>小于</strong>当前节点的数。</li>
	<li>节点的右子树只包含<strong>大于</strong>当前节点的数。</li>
	<li>所有左子树和右子树自身必须也是二叉搜索树。</li>
</ul>

<p><strong>示例&nbsp;1:</strong></p>

<pre><strong>输入:</strong>
    2
   / \
  1   3
<strong>输出:</strong> true
</pre>

<p><strong>示例&nbsp;2:</strong></p>

<pre><strong>输入:
</strong>    5
   / \
  1   4
&nbsp;    / \
&nbsp;   3   6
<strong>输出:</strong> false
<strong>解释:</strong> 输入为: [5,1,4,null,null,3,6]。
&nbsp;    根节点的值为 5 ，但是其右子节点值为 4 。
</pre>


## 解法：

首先想到的是根据二叉树的性质，即左子树中的值小于根节点的值，右子树中的值大于根节点的值。这样以来，对于每个节点，都有一个取值范围。比如某个左孩子的右孩子节点，它的值需要大于父节点，但要小于根节点。


```
    20
   /
 10
   \
    15
```


```python
class Solution:
    def isValidBST(self, root):
        inf = float('inf')

        return self._isValidBST(root, max=inf, min=-inf)

    def _isValidBST(self, node, max, min):
        if not node:
            return True

        if not (min < node.val < max):
            return False

        if not self._isValidBST(node.left, min=min, max=node.val):
            return False

        if not self._isValidBST(node.right, min=node.val, max=max):
            return False
        
        return True
```


后来看别人提到一种更加巧妙的方法，一个二叉树查找树的中序遍历，是升序的。

```python
class Solution:
    def isValidBST(self, root):
        stack = []
        node = root
        last = float('-inf')
        
        while stack or node:
            while node:
                stack.append(node)
                node = node.left

            node = stack.pop()
            if last >= node.val:
                return False
            last = node.val
            
            node = node.right
        
        return True
```