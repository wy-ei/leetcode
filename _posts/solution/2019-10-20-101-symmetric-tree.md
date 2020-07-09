---
title: 对称二叉树
qid: 101
tags: [树,深度优先搜索,广度优先搜索]
---


- 难度： 简单
- 通过率： 42.2%
- 题目链接：[https://leetcode-cn.com/problems/symmetric-tree](https://leetcode-cn.com/problems/symmetric-tree)


## 题目描述

来源于 [https://leetcode-cn.com/](https://leetcode-cn.com/)

<p>给定一个二叉树，检查它是否是镜像对称的。</p>

<p>例如，二叉树&nbsp;<code>[1,2,2,3,4,4,3]</code> 是对称的。</p>

<pre>    1
   / \
  2   2
 / \ / \
3  4 4  3
</pre>

<p>但是下面这个&nbsp;<code>[1,2,2,null,3,null,3]</code> 则不是镜像对称的:</p>

<pre>    1
   / \
  2   2
   \   \
   3    3
</pre>

<p><strong>说明:</strong></p>

<p>如果你可以运用递归和迭代两种方法解决这个问题，会很加分。</p>


## 解法：

```c++
class Solution {
public:
    bool isSymmetric(TreeNode* root) {
        if(root == nullptr){
            return true;
        }
        return isSymmetric(root->left, root->right);
    }

private:

    bool isSymmetric(TreeNode* node1, TreeNode* node2){
        if(node1 == nullptr && node2 == nullptr){
            return true;
        }
        if(node1 == nullptr || node2 == nullptr){
            return false;
        }
        if(node1->val != node2->val){
            return false;
        }
        return isSymmetric(node1->left, node2->right)
            && isSymmetric(node1->right, node2->left);
    }
};
```