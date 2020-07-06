---
title: 从前序与中序遍历序列构造二叉树
qid: 105
tags: [树,深度优先搜索,数组]
---


- 难度： 中等
- 通过率： 38.4%
- 题目链接：[https://leetcode-cn.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal](https://leetcode-cn.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal)


## 题目描述

来源于 [https://leetcode-cn.com/](https://leetcode-cn.com/)

<p>根据一棵树的前序遍历与中序遍历构造二叉树。</p>

<p><strong>注意:</strong><br>
你可以假设树中没有重复的元素。</p>

<p>例如，给出</p>

<pre>前序遍历 preorder =&nbsp;[3,9,20,15,7]
中序遍历 inorder = [9,3,15,20,7]</pre>

<p>返回如下的二叉树：</p>

<pre>    3
   / \
  9  20
    /  \
   15   7</pre>


## 解法：

先序遍历的第一个元素，为树的根节点，而后是左子树中的各个节点，之后是右子树的各个节点。

先序遍历的第一个值可以将中序遍历的列表分成左右子树。以题目描述中的树为例，`3` 把中序遍历的序列中分为 `[9]` 和 `[15, 20, 7]`。

构造过程递归地进行，不断地从 preorder 的前端取值，作为根节点的值。切分了左右子树的序列，判断序列是否为空，为空则停止递归。

```python
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        if not inorder:
            return None
            
        root = TreeNode(preorder[0])

        i = inorder.index(root.val)
        root.left = self.buildTree(preorder[1:i+i], inorder[:i])
        root.right = self.buildTree(preorder[i+1:], inorder[i+1:])
        
        return root    
```