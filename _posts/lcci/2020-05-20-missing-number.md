---
title: 消失的数字
qid: 17.04
tags: [位运算,数组,数学]
---


- 难度：Easy
- 题目链接：[https://leetcode-cn.com/problems/missing-number-lcci/](https://leetcode-cn.com/problems/missing-number-lcci/)


## 题目描述

来源于 [https://leetcode-cn.com/](https://leetcode-cn.com/)

<p>数组<code>nums</code>包含从<code>0</code>到<code>n</code>的所有整数，但其中缺了一个。请编写代码找出那个缺失的整数。你有办法在O(n)时间内完成吗？</p>

<p><strong>注意：</strong>本题相对书上原题稍作改动</p>

<p><strong>示例 1：</strong></p>

<pre><strong>输入：</strong>[3,0,1]
<strong>输出：</strong>2</pre>

<p>&nbsp;</p>

<p><strong>示例 2：</strong></p>

<pre><strong>输入：</strong>[9,6,4,2,3,5,7,0,1]
<strong>输出：</strong>8
</pre>


## 解法一：使用下标标记


```c++
class Solution {
public:
    int missingNumber(vector<int>& nums) {
        int len = nums.size();
        const int MAX_INT = numeric_limits<int>::max();
        for(int i=0;i<len;i++){
            int n = nums[i];
            if(n < 0){
                n += MAX_INT;
            }
            if(n < len && nums[n] >= 0){
                nums[n] -= MAX_INT;
            }
        }

        for(int i=0;i<len;i++){
            if(nums[i] >= 0){
                return i;
            }
        }
        return len;
    }
};
```

## 解法二：异或

因为不存在重复的数字，而且范围在 `[0,n]` 之间。对于出现过的数，下标 i 和这个数本身异或之后会清零。

```c++
class Solution {
public:
    int missingNumber(vector<int>& nums) {
        int x = nums.size();
        for(int i=0;i<nums.size();i++){
            x ^= i ^ nums[i];
        }
        return x;
    }
};
```