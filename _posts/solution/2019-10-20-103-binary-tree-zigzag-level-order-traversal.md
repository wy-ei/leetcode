---
title: 二叉树的锯齿形层次遍历
qid: 103
tags: [栈,树,广度优先搜索]
---


- 难度： 中等
- 通过率： 39.6%
- 题目链接：[https://leetcode-cn.com/problems/binary-tree-zigzag-level-order-traversal](https://leetcode-cn.com/problems/binary-tree-zigzag-level-order-traversal)


## 题目描述

来源于 [https://leetcode-cn.com/](https://leetcode-cn.com/)

<p>给定一个二叉树，返回其节点值的锯齿形层次遍历。（即先从左往右，再从右往左进行下一层遍历，以此类推，层与层之间交替进行）。</p>

<p>例如：<br>
给定二叉树&nbsp;<code>[3,9,20,null,null,15,7]</code>,</p>

<pre>    3
   / \
  9  20
    /  \
   15   7
</pre>

<p>返回锯齿形层次遍历如下：</p>

<pre>[
  [3],
  [20,9],
  [15,7]
]
</pre>


## 解法：

先进行层次遍历，然后根据层数来翻转。

```cpp
class Solution {
public:
    vector<vector<int>> zigzagLevelOrder(TreeNode *root) {
        vector<vector<int>> res;
        queue<TreeNode *> queue_;
        if (root) {
            queue_.push(root);
        }

        int level = 0;
        while (!queue_.empty()) {
            int size = queue_.size();
            vector<int> nums;
            for (int i = 0; i < size; i++) {
                TreeNode *node = queue_.front();
                queue_.pop();
                nums.push_back(node->val);
                if (node->left) {
                    queue_.push(node->left);
                }
                if (node->right) {
                    queue_.push(node->right);
                }
            }
            if (level & 1 == 1) {
                reverse(nums.begin(), nums.end());
            }
            res.push_back(::move(nums));
            level += 1;
        }
        return res;
    }
};
```