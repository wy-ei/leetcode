---
title: 二叉树的层序遍历
qid: 102
tags: [树,广度优先搜索]
---


- 难度： 中等
- 通过率： 46.1%
- 题目链接：[https://leetcode-cn.com/problems/binary-tree-level-order-traversal](https://leetcode-cn.com/problems/binary-tree-level-order-traversal)


## 题目描述

来源于 [https://leetcode-cn.com/](https://leetcode-cn.com/)

<p>给定一个二叉树，返回其按层次遍历的节点值。 （即逐层地，从左到右访问所有节点）。</p>

<p>例如:<br>
给定二叉树:&nbsp;<code>[3,9,20,null,null,15,7]</code>,</p>

<pre>    3
   / \
  9  20
    /  \
   15   7
</pre>

<p>返回其层次遍历结果：</p>

<pre>[
  [3],
  [9,20],
  [15,7]
]
</pre>


## 基于队列的解法

维护一个队列，从根节点开始遍历二叉树，遇到一个节点后就将其放入队列，下次遍历的节点，从队列的头部取。这样得到的效果就是，先入队的先被访问，即先访问第一层，而后第二层，以此类推。最终就实现了层次遍历。

如果一次出队一个节点，为了区别节点的层级，需要加入层级信息。其实没有必要。可以一次性把同一层的节点全部出队并处理。

```cpp
class Solution {
  public:
    vector<vector<int>> levelOrder(TreeNode *root) {
        vector<vector<int>> res;
        queue<TreeNode *> queue_;
        if(root){
            queue_.push(root);
        }

        while(!queue_.empty()){
            int size = queue_.size();
            vector<int> nums;
            for (size_t i = 0; i < size; i++){
                TreeNode* node = queue_.front();
                queue_.pop();
                nums.push_back(node->val);
                if(node->left){
                    queue_.push(node->left);
                }
                if(node->right){
                    queue_.push(node->right);
                }
            }
            res.push_back(::move(nums));
        }

        return res;
    }
};
```

## 递归解法

从根节点起，采用先序遍历，记录每个节点的层级，把节点的值插入对应层级的数组中。

```cpp
class Solution {
  public:
    vector<vector<int>> levelOrder(TreeNode *root) {
        vector<vector<int>> res;
        traverse(root, 1, res);
        return res;
    }

    void traverse(TreeNode *root, size_t level, vector<vector<int>> &res) {
        if (!root) {
            return;
        }
        if (res.size() < level) {
            res.emplace_back();
        }
        res[level-1].push_back(root->val);
        traverse(root->left, level + 1, res);
        traverse(root->right, level + 1, res);
    }
};
```