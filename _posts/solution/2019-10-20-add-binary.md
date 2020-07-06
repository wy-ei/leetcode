---
title: 二进制求和
qid: 67
tags: [数学,字符串]
---


- 难度： 简单
- 通过率： 37.1%
- 题目链接：[https://leetcode-cn.com/problems/add-binary](https://leetcode-cn.com/problems/add-binary)


## 题目描述

来源于 [https://leetcode-cn.com/](https://leetcode-cn.com/)

<p>给定两个二进制字符串，返回他们的和（用二进制表示）。</p>

<p>输入为<strong>非空</strong>字符串且只包含数字&nbsp;<code>1</code>&nbsp;和&nbsp;<code>0</code>。</p>

<p><strong>示例&nbsp;1:</strong></p>

<pre><strong>输入:</strong> a = &quot;11&quot;, b = &quot;1&quot;
<strong>输出:</strong> &quot;100&quot;</pre>

<p><strong>示例&nbsp;2:</strong></p>

<pre><strong>输入:</strong> a = &quot;1010&quot;, b = &quot;1011&quot;
<strong>输出:</strong> &quot;10101&quot;</pre>


## 解法：

逐项相加向前进位即可。

```python
class Solution:
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        cy = 0
        bits = []

        i = len(a) - 1
        j = len(b) - 1
        while i >= 0 or j >= 0:
            if i < 0:
                bit_a = 0
            else:
                bit_a = int(a[i])
                
            if j < 0:
                bit_b = 0
            else:
                bit_b = int(b[j])
            
            i -= 1
            j -= 1
            
            bit_sum = (bit_a + bit_b + cy)
            cy = bit_sum // 2
            bits.append(bit_sum % 2)
            
        if cy:
            bits.append(cy)
        
        return ''.join(map(str, bits[::-1]))
```