---
title: 首个共同祖先
qid: 04.08
tags: [树]
---


- 难度：Medium
- 题目链接：[https://leetcode-cn.com/problems/first-common-ancestor-lcci/](https://leetcode-cn.com/problems/first-common-ancestor-lcci/)


## 题目描述

来源于 [https://leetcode-cn.com/](https://leetcode-cn.com/)

<p>设计并实现一个算法，找出二叉树中某两个节点的第一个共同祖先。不得将其他的节点存储在另外的数据结构中。注意：这不一定是二叉搜索树。</p>

<p>例如，给定如下二叉树: root = [3,5,1,6,2,0,8,null,null,7,4]</p>

<pre>    3
   / \
  5   1
 / \ / \
6  2 0  8
  / \
 7   4
</pre>

<p><strong>示例 1:</strong></p>

<pre><strong>输入:</strong> root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 1
<strong>输出:</strong> 3
<strong>解释:</strong> 节点 5 和节点 1 的最近公共祖先是节点 3。</pre>

<p><strong>示例 2:</strong></p>

<pre><strong>输入:</strong> root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 4
<strong>输出:</strong> 5
<strong>解释:</strong> 节点 5 和节点 4 的最近公共祖先是节点 5。因为根据定义最近公共祖先节点可以为节点本身。</pre>

<p><strong>说明:</strong></p>

<pre>所有节点的值都是唯一的。
p、q 为不同节点且均存在于给定的二叉树中。</pre>


## 解法：

后序遍历，在二叉树中寻找 `p` 和 `q` 两个节点，如果找到任意一个就返回它。在左右子树中寻找之后，如果发现左右两个子树中均能找到其中一个，那当前节点一定是最近的公共祖先，返回之。否则，递归向上回退。

在遍历过程中，一旦找到了 `p` 和 `q` 中的一个，就不用在深入下去了。假如 `p` 和 `q` 中一个为父节点，一个为某个孩子节点，上一段提到的那种情况就不会出现，此时返回找到的第一个 `p` 或 `q` 即可。

```c++
class Solution {
public:
    TreeNode* lowestCommonAncestor(TreeNode* root, TreeNode* p, TreeNode* q) {
        if(root == nullptr) return nullptr;

        if(root == p || root == q){
            return root;
        }

        TreeNode *left = lowestCommonAncestor(root->left, p, q);
        TreeNode *right = lowestCommonAncestor(root->right, p, q);

        if(left && right){
            return root;
        }

        if(left){
            return left;
        }

        if(right){
            return right;
        }

        return nullptr;
    }
};
```