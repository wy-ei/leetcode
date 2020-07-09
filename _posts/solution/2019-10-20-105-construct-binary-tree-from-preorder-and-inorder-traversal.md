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

前序遍历，访问顺序为：根节点->左节点->右节点。中序遍历，访问顺序为：左节点->根节点->右节点。

前序遍历的第一个节点一定是根节点，根据这个根节点的值，可以把中序遍历结果分为左右两个部分，左边的就是左子树，右边是右子树。

左子树的根节点，自然就是前序遍历的第二个元素了，根据根节点的值，可以再次把左子树分为两个部分。因此，从前序遍历的前端 pop 一个值，划分左右子树。然后先重建左子树，根节点的值从前序遍历的前面 pop 即可。左子树为空的时候，开始重建右子树，右子树的根节点还是从前序遍历的前端 pop 一个值。

```cpp
class Solution {
    using iterator = vector<int>::iterator;
public:
    TreeNode* buildTree(vector<int>& preorder, vector<int>& inorder) {
        auto pre = deque<int>(preorder.begin(), preorder.end());
        TreeNode* root = buildTree(inorder.begin(), inorder.end(), pre);
        return root;
    }

    TreeNode* buildTree(iterator first, iterator last, deque<int>& preorder) {
        if(first == last){
            return nullptr;
        }
        
        int root = preorder.front();
        preorder.pop_front();
        
        TreeNode *node = new TreeNode(root); 
        auto it = find(first, last, root);
        node->left = buildTree(first, it, preorder);
        node->right = buildTree(it+1, last, preorder);
        
        return node;
    }
};
```