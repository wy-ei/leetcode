---
title: 二叉树的中序遍历
qid: 94
tags: [栈,树,哈希表]
---


- 难度： 中等
- 通过率： 53.9%
- 题目链接：[https://leetcode-cn.com/problems/binary-tree-inorder-traversal](https://leetcode-cn.com/problems/binary-tree-inorder-traversal)


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

### 递归解法

```c++
class Solution {
  public:
    vector<int> inorderTraversal(TreeNode* root){
        vector<int> res;
        traversal(root, res);
        return res;
    }

    void traversal(TreeNode *node, vector<int>& res) {
        if (!node){
            return;
        }

        traversal(node->left, res);
        res.push_back(node->val);
        traversal(node->right, res);
    }
};
```

### 基于栈的迭代解法


```cpp
class Solution {
public:
    vector<int> inorderTraversal(TreeNode *root) {
        vector<int> res;
        stack<TreeNode*> stk;
        TreeNode* node = root;

        while(node || !stk.empty()){
            while(node){
                stk.push(node);
                node = node->left;
            }
            node = stk.top();
            stk.pop();
            res.push_back(node->val);
            node = node->right;
        }
        return res;
    }
};
```