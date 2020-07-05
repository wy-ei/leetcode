---
title: Maximum XOR of Two Numbers in an Array
qid: 421
---


- 难度： 中等
- 通过率： 49.8%
- 题目链接：[https://leetcode.com/problems/maximum-xor-of-two-numbers-in-an-array](https://leetcode.com/problems/maximum-xor-of-two-numbers-in-an-array)


## 题目描述

来源于 [https://leetcode-cn.com/](https://leetcode-cn.com/)

<p>给定一个非空数组，数组中元素为 a<sub>0</sub>, a<sub>1</sub>, a<sub>2</sub>, &hellip; , a<sub>n-1</sub>，其中 0 &le; a<sub>i</sub> &lt; 2<sup>31&nbsp;</sup>。</p>

<p>找到 a<sub>i</sub> 和a<sub>j&nbsp;</sub>最大的异或 (XOR) 运算结果，其中0 &le; <em>i</em>,&nbsp;&nbsp;<em>j</em> &lt; <em>n&nbsp;</em>。</p>

<p>你能在O(<em>n</em>)的时间解决这个问题吗？</p>

<p><strong>示例:</strong></p>

<pre>
<strong>输入:</strong> [3, 10, 5, 25, 2, 8]

<strong>输出:</strong> 28

<strong>解释:</strong> 最大的结果是 <strong>5</strong> ^ <strong>25</strong> = 28.
</pre>


## 解法：


```cpp
class Solution {
    struct Node{
        Node *next[2]{nullptr};
    };

public:
    int findMaximumXOR(vector<int>& nums) {
        Node *root = new Node;
        for(int num: nums){
            insert(num, root);
        }

        int max_xor = 0;
        for(int num: nums){
            int xor_value = find_max_xor(num, root);
            max_xor = max(max_xor, xor_value);
        }

        // destory(root);
        return max_xor;
    }

    void insert(int num, Node *root){
        int mask = 1 << 31;
        for(int i=31;i>=0;i--){
            int index = num & (1 << i) ? 1 : 0;
            if(root->next[index] == nullptr){
                root->next[index] = new Node;
            }
            root = root->next[index];
        }
    }

    int find_max_xor(int num, Node *root){
        int xor_value = 0;
        for(int i=31;i>=0;i--){
            int index = num & (1 << i) ? 1 : 0;
            if(root->next[1-index] != nullptr){
                root = root->next[1-index];
                xor_value += (1 << i);
            }else{
                root = root->next[index];
            }
        }
        return xor_value;
    }
};
```