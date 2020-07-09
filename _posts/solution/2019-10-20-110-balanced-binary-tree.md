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

这个问题可以递归地去检查子树的是否平衡，深度的计算应该是从树的叶子开始，然后复用子树的求得的深度一些解法，直接去求子树的深度，但是没有复用深度，造成了很多没必要的计算。

这里一个困难点在于，如何在计算深度的同时，向外层传递不平衡的信息，以便在发现不平衡时，算法可以立刻停止。这里我使用了异常机制，在出现不平衡后断言不成立，会抛出异常。

递归地计算左右子树的深度，发现不平衡后，抛出异常，由此立刻退出递归调用。

```c++
class Solution {
public:
    bool isBalanced(TreeNode* root) {
        try{
            throw_if_unbalance(root);
            return true;
        }catch(...){
            return false;
        }
    }
private:
    int throw_if_unbalance(TreeNode* node) {
        if(node == nullptr){
            return 0;
        }

        int left_depth = throw_if_unbalance(node->left);
        int right_depth = throw_if_unbalance(node->right);

        if(abs(left_depth - right_depth) > 1){
            throw exception();
        }
        return 1 + max(left_depth, right_depth);
    }
};
```