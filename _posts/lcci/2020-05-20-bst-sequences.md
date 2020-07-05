---
title: 二叉搜索树序列
qid: 04.09
tags: [树,动态规划]
---


- 难度：Hard
- 题目链接：[https://leetcode-cn.com/problems/bst-sequences-lcci/](https://leetcode-cn.com/problems/bst-sequences-lcci/)


## 题目描述

来源于 [https://leetcode-cn.com/](https://leetcode-cn.com/)

<p>从左向右遍历一个数组，通过不断将其中的元素插入树中可以逐步地生成一棵二叉搜索树。给定一个由不同节点组成的二叉树，输出所有可能生成此树的数组。</p>

<p><strong>示例:</strong><br>
给定如下二叉树</p>

<pre>        2
       / \
      1   3
</pre>

<p>返回:</p>

<pre>[
   [2,1,3],
   [2,3,1]
]
</pre>


## 解法：

根节点出现必须在子节点之前，每一棵子树，其左右孩子的序列可以互相穿插。即左右子树节点序列中的前后顺序不能改变，但是两个子树的序列可以穿插在一起。

数组 a 和 b 的穿插，就像洗扑克牌一样，a 和 b 内部的元素的前后顺序不能打乱，这看起来是很复杂的任务。想象如下手动洗扑克牌的过程，把扑克分成均匀两部分，然后两个大拇指决定释放那边的扑克。如果能够控制左右手释放扑克的顺序，也就能控制穿插的结果了。为此我想到了这样的算法：使用一个长度为 54 的数组 c，其中一半为 0 一半为 1。然后遍历数组 c，遇到 1 就释放左手边的牌，遇到 0 就释放右手边的牌。然后对数组 c 做 permutation，继续前述操作。如此就可以得到所有的穿插方案了。


```c++
class Solution {
public:
    vector<vector<int>> BSTSequences(TreeNode* root) {
        vector<vector<int>> ret;

        if(root == nullptr){
            ret.push_back(vector<int>());
            return ret;
        }

        auto left = BSTSequences(root->left);
        auto right = BSTSequences(root->right);

        ret = mix(left, right, root->val);

        return ret;
    }

private:
    vector<vector<int>> mix(vector<vector<int>>& left, vector<vector<int>>& right, int root){
        vector<vector<int>> ret;
        ret.reserve(left.size() * right.size());

        for(auto &l: left){
            for(auto &r: right){
                do_mix(l, r, root, ret);
            }
        }
        return ret;
    }

    void do_mix(vector<int>& left, vector<int>& right, int root, vector<vector<int>>& ret){
        if(left.empty() && right.empty()){
            ret.push_back(vector<int>{root});
            return;    
        }
        vector<int> bits(left.size() + right.size(), 1);
        fill(bits.begin(), bits.begin() + left.size(), 0);

        do{
            int i = 0, j = 0;
            vector<int> mixed_vec;
            mixed_vec.reserve(bits.size()+1);
            mixed_vec.push_back(root);
            for(auto bit: bits){
                if(bit == 0){
                    mixed_vec.push_back(left[i++]);
                }else{
                    mixed_vec.push_back(right[j++]);
                }
            }
            ret.emplace_back(::move(mixed_vec));
        } while (next_permutation(bits.begin(), bits.end()));
    }
};
```