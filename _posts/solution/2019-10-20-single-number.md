---
title: 只出现一次的数字
qid: 136
tags: [位运算,哈希表]
---


- 难度： 简单
- 通过率： 58.1%
- 题目链接：[https://leetcode-cn.com/problems/single-number](https://leetcode-cn.com/problems/single-number)


## 题目描述

来源于 [https://leetcode-cn.com/](https://leetcode-cn.com/)

<p>给定一个<strong>非空</strong>整数数组，除了某个元素只出现一次以外，其余每个元素均出现两次。找出那个只出现了一次的元素。</p>

<p><strong>说明：</strong></p>

<p>你的算法应该具有线性时间复杂度。 你可以不使用额外空间来实现吗？</p>

<p><strong>示例 1:</strong></p>

<pre><strong>输入:</strong> [2,2,1]
<strong>输出:</strong> 1
</pre>

<p><strong>示例&nbsp;2:</strong></p>

<pre><strong>输入:</strong> [4,1,2,1,2]
<strong>输出:</strong> 4</pre>


## 解法：


- 异或满足交换律：a ^ b ^ c <=> a ^ c ^ b
- 任何数与 0 异或还是这个数： 0 ^ n => n
- 相同的数异或结果为 0：n ^ n => 0


```python
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        xor = 0
        for num in nums:
            xor ^= num
        return xor
```