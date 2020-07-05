---
title: 翻转数位
qid: 05.03
tags: [位运算]
---


- 难度：Easy
- 题目链接：[https://leetcode-cn.com/problems/reverse-bits-lcci/](https://leetcode-cn.com/problems/reverse-bits-lcci/)


## 题目描述

来源于 [https://leetcode-cn.com/](https://leetcode-cn.com/)

<p>给定一个32位整数 <code>num</code>，你可以将一个数位从0变为1。请编写一个程序，找出你能够获得的最长的一串1的长度。</p>

<p><strong>示例 1：</strong></p>

<pre><strong>输入:</strong> <code>num</code> = 1775(11011101111<sub>2</sub>)
<strong>输出:</strong> 8
</pre>

<p><strong>示例 2：</strong></p>

<pre><strong>输入:</strong> <code>num</code> = 7(0111<sub>2</sub>)
<strong>输出:</strong> 4
</pre>


## 解法：

统计前一段连续的 1 的个数，以及后一段连续 1 的个数，两者之和 + 1 就是翻转一个 0->1 后连续 1 的个数。 

```c++
class Solution {
public:
    int reverseBits(int num) {
        if(num == -1) return 32;
        
        unsigned int n = num;
        int prev = 0, curr = 0;
        int ret = 0;

        while(n){
            if(n & 1){
                curr++;
            }else{
                prev = curr;
                curr = 0;
            }
            ret = max(prev + curr, ret);
            n = n >> 1;
        }
        return ret + 1;
    }
};
```