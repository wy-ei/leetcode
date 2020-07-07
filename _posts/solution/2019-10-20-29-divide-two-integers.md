---
title: 两数相除
qid: 29
tags: [数学,二分查找]
---


- 难度： 中等
- 通过率： 15.9%
- 题目链接：[https://leetcode-cn.com/problems/divide-two-integers](https://leetcode-cn.com/problems/divide-two-integers)


## 题目描述

<p>给定两个整数，被除数&nbsp;<code>dividend</code>&nbsp;和除数&nbsp;<code>divisor</code>。将两数相除，要求不使用乘法、除法和 mod 运算符。</p>

<p>返回被除数&nbsp;<code>dividend</code>&nbsp;除以除数&nbsp;<code>divisor</code>&nbsp;得到的商。</p>

<p><strong>示例&nbsp;1:</strong></p>

<pre><strong>输入:</strong> dividend = 10, divisor = 3
<strong>输出:</strong> 3</pre>

<p><strong>示例&nbsp;2:</strong></p>

<pre><strong>输入:</strong> dividend = 7, divisor = -3
<strong>输出:</strong> -2</pre>

<p><strong>说明:</strong></p>

<ul>
	<li>被除数和除数均为 32 位有符号整数。</li>
	<li>除数不为&nbsp;0。</li>
	<li>假设我们的环境只能存储 32 位有符号整数，其数值范围是 [&minus;2<sup>31</sup>,&nbsp; 2<sup>31&nbsp;</sup>&minus; 1]。本题中，如果除法结果溢出，则返回 2<sup>31&nbsp;</sup>&minus; 1。</li>
</ul>


## 解法：

不使用乘法、除法和 mod 运算符来完成除法，那么就只能使用减法了，一种方法是先将除数和被除数都转换为正数，然后不断地从被除数中减去除数，减一个除数商就加一。但是这种方法显得太慢了，因此考虑在迭代中倍增除数，这样商就可以每次 +1 +2 +4 ...。在某一时刻，当被除数小于除数的时候，把除数还原。

```c++
class Solution {
public:
    int divide(int dividend, int divisor) {
        long long m = dividend;
        long long n = divisor;
        int sign = (m < 0) ^ (n < 0) ? -1 : 1;
        m = abs(m);
        n = abs(n);

        long long result = 0;
        while(m >= n){
            long long a = 1;
            long long nn = n;
            while(m >= nn){
                m -= nn;
                result += a;
                nn = nn << 1;
                a = a << 1;
            }
        }

        if(sign == 1 && result > INT_MAX){
            return INT_MAX;
        }else if(sign == -1 && result < INT_MIN){
            return INT_MAX;
        }else{
            return result * sign;
        }
    }
};
```