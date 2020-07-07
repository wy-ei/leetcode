---
title: 字符串相乘
qid: 43
tags: [数学,字符串]
---


- 难度： 中等
- 通过率： 29.5%
- 题目链接：[https://leetcode-cn.com/problems/multiply-strings](https://leetcode-cn.com/problems/multiply-strings)


## 题目描述

来源于 [https://leetcode-cn.com/](https://leetcode-cn.com/)

<p>给定两个以字符串形式表示的非负整数&nbsp;<code>num1</code>&nbsp;和&nbsp;<code>num2</code>，返回&nbsp;<code>num1</code>&nbsp;和&nbsp;<code>num2</code>&nbsp;的乘积，它们的乘积也表示为字符串形式。</p>

<p><strong>示例 1:</strong></p>

<pre><strong>输入:</strong> num1 = &quot;2&quot;, num2 = &quot;3&quot;
<strong>输出:</strong> &quot;6&quot;</pre>

<p><strong>示例&nbsp;2:</strong></p>

<pre><strong>输入:</strong> num1 = &quot;123&quot;, num2 = &quot;456&quot;
<strong>输出:</strong> &quot;56088&quot;</pre>

<p><strong>说明：</strong></p>

<ol>
	<li><code>num1</code>&nbsp;和&nbsp;<code>num2</code>&nbsp;的长度小于110。</li>
	<li><code>num1</code> 和&nbsp;<code>num2</code> 只包含数字&nbsp;<code>0-9</code>。</li>
	<li><code>num1</code> 和&nbsp;<code>num2</code>&nbsp;均不以零开头，除非是数字 0 本身。</li>
	<li><strong>不能使用任何标准库的大数类型（比如 BigInteger）</strong>或<strong>直接将输入转换为整数来处理</strong>。</li>
</ol>


## 解法 1：

这个题考察了乘法的原理，在手动计算乘法的时候，每乘完一次，就尝试进位。但其实可以在最后进行进位。

```
     7  7  8
x       6  7
------------
    49 49 56 <-- 7 * 778 
 42 42 48    <-- 6 * 778
------------ <-- 各项做加法
 42 91 97 56 <-- 56 向前进位得到 97+5=102 余下 6
------------
 42 91 102 6 <-- 102 向前进位得到 91+10=101 余下 2
------------
 42 101  2 6 <-- 101 向前进位得到 42+10=52 余下 1
------------
 52   1  2 6 <-- 52 向前进位得到 0+5=5 余下 2
------------
5 2   1  2 6 --> 最终结果 52126
```

采用这个方法来做乘法，再大的数也不会产生溢出。但是在 Python 中，这个方法不如直接使用 `str(int(num1) * int(num2))` 的速度快。


```python
def multiply(num1, num2):
    """
    :type num1: str
    :type num2: str
    :rtype: str
    """
    if num1 == '0' or num2 == '0':
        return '0'

    result = [0 for _ in range(len(num1) + len(num2))]

    for i in range(len(num1)):
        for j in range(len(num2)):
            result[i+j+1] += int(num1[i]) * int(num2[j])

    carry = 0
    for i in range(len(result) - 1, -1, -1):
        n = result[i] + carry
        carry = n // 10
        result[i] = n % 10

    if result[0] == 0:
        result.pop(0)

    return ''.join(map(str, result))
```

## 解法 2：

[在 leetcode 讨论区](https://leetcode-cn.com/problems/multiply-strings/discuss/17605/Easiest-JAVA-Solution-with-Graph-Explanation)看到另一个思路。

```
        7 7 8
 x        6 7
-------------
      5 4 4 6
 +  4 6 6 8
-------------
    5 2 1 2 6
```

结果长度为 `len(num1) + len(num2)` 或者 `len(num1) + len(num2) - 1`（没有产生进位）。另外 `num1[i]` 和 `num2[j]` 中每一位相乘，结果的十位和个位，在最终结果中的位置和 `i` 和 `j` 是有关系的。

十位会放在 `i+j` 处，个位会放在 `i+j+1` 处。所有可以直接把相乘结果的个位和十位放到相应的位置，并对个位的和先前进位。

```python
def multiply2(self, num1, num2):
    num1 = list(map(int, num1))
    num2 = list(map(int, num2))

    pos = [0 for _ in range(len(num1) + len(num2))]

    for i in range(len(num1)-1, -1, -1):
        for j in range(len(num2)-1, -1, -1):

            mul = num1[i] * num2[j]
            p1 = i + j
            p2 = i + j + 1

            n = mul + pos[p2]
            pos[p1] += n // 10
            pos[p2] = n % 10

    if pos[0] == 0:
        pos.pop(0)

    return ''.join(map(str, pos))
```