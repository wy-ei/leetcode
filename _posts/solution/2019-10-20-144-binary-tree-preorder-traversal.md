---
title: 二叉树的前序遍历
qid: 144
tags: [栈,树]
---


- 难度： 中等
- 通过率： 49.5%
- 题目链接：[https://leetcode-cn.com/problems/binary-tree-preorder-traversal](https://leetcode-cn.com/problems/binary-tree-preorder-traversal)


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


## 递归解法：

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
        res.push_back(node->val);
        traversal(node->left, res);
        traversal(node->right, res);
    }
};
```

## 基于栈的解法

```cpp
class Solution {
  public:
    vector<int> preorderTraversal(TreeNode *root) {
        vector<int> res;
        stack<TreeNode*> stk;
        if(root){
            stk.push(root);
        }

        while(!stk.empty()){
            TreeNode *node = stk.top();
            stk.pop();
            while(node){
                res.push_back(node->val);
                if(node->right){
                    stk.push(node->right);
                }
                node = node->left;
            }
        }
        return res;
    }
};
```