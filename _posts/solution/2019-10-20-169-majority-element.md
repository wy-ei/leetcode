---
title: 多数元素
qid: 169
tags: [位运算,数组,分治算法]
---


- 难度： 简单
- 通过率： 50.7%
- 题目链接：[https://leetcode-cn.com/problems/majority-element](https://leetcode-cn.com/problems/majority-element)


## 题目描述

来源于 [https://leetcode-cn.com/](https://leetcode-cn.com/)

<p>给定一个大小为 <em>n </em>的数组，找到其中的众数。众数是指在数组中出现次数<strong>大于</strong>&nbsp;<code>&lfloor; n/2 &rfloor;</code>&nbsp;的元素。</p>

<p>你可以假设数组是非空的，并且给定的数组总是存在众数。</p>

<p><strong>示例&nbsp;1:</strong></p>

<pre><strong>输入:</strong> [3,2,3]
<strong>输出:</strong> 3</pre>

<p><strong>示例&nbsp;2:</strong></p>

<pre><strong>输入:</strong> [2,2,1,1,1,2,2]
<strong>输出:</strong> 2
</pre>


## 解法：

这道题，最直白的解法是使用一个 map 来记录各个数字出现的次数，最后取出现次数最多的作为解。但这个方法需要消耗额外的空间，不是最优。

参考评论区的解答，看到了一种叫做“摩尔投票法”的解答，仔细一想，相当厉害。

想象一个投票的场景，只有某个选项的投票人数超过总人数的一半时，此选项才能通过。

```python
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count = 0
        ret = float('nan')
        
        for num in nums:
            if ret == num:
                count += 1
            else:
                count -= 1
                
                if count < 0:
                    ret = num
                    count = 1
        return ret
```