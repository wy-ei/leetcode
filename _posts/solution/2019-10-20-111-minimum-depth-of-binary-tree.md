---
title: 二叉树的最小深度
qid: 111
tags: [树,深度优先搜索,广度优先搜索]
---


- 难度： 简单
- 通过率： 34.5%
- 题目链接：[https://leetcode-cn.com/problems/minimum-depth-of-binary-tree](https://leetcode-cn.com/problems/minimum-depth-of-binary-tree)


## 题目描述

来源于 [https://leetcode-cn.com/](https://leetcode-cn.com/)

<p>给定一个二叉树，找出其最小深度。</p>

<p>最小深度是从根节点到最近叶子节点的最短路径上的节点数量。</p>

<p><strong>说明:</strong>&nbsp;叶子节点是指没有子节点的节点。</p>

<p><strong>示例:</strong></p>

<p>给定二叉树&nbsp;<code>[3,9,20,null,null,15,7]</code>,</p>

<pre>    3
   / \
  9  20
    /  \
   15   7</pre>

<p>返回它的最小深度 &nbsp;2.</p>


## 解法：

层次遍历，遇到第一个没有左右孩子的节点时停止。

```c++
class Solution {
public:
    int minDepth(TreeNode* root) {
        queue<TreeNode *> queue_;
        if(root){
            queue_.push(root);
        }
        int level = 0;
        while(!queue_.empty()){
            level += 1;
            int size = queue_.size();
            for (size_t i = 0; i < size; i++){
                TreeNode* node = queue_.front();
                queue_.pop();

                if(!node->left && !node->right){
                    return level;
                }

                if(node->left){
                    queue_.push(node->left);
                }
                if(node->right){
                    queue_.push(node->right);
                }
            }
        }
        return level;
    }
};
```

深度优先遍历也行：

```cpp
class Solution {
public:
    int minDepth(TreeNode* root) {
        if(!root) return 0;
        int min_depth = INT_MAX;
        traversal(root, 1, &min_depth);
        return min_depth;
    }

    void traversal(TreeNode *node, int depth, int *min_depth) {
        if (!node){
            return;
        }
        if(!node->left && !node->right){
            *min_depth = min(*min_depth, depth);
        }
        if(depth == *min_depth){
            // 剪枝
            return;
        }
        traversal(node->left, depth + 1, min_depth);
        traversal(node->right, depth + 1, min_depth);
    }
};
```

