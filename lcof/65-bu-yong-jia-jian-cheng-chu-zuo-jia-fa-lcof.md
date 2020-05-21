## 65. 不用加减乘除做加法

- 难度：Easy
- 题目链接：[https://leetcode-cn.com/problems/bu-yong-jia-jian-cheng-chu-zuo-jia-fa-lcof/](https://leetcode-cn.com/problems/bu-yong-jia-jian-cheng-chu-zuo-jia-fa-lcof/)


## 题目描述

来源于 [https://leetcode-cn.com/](https://leetcode-cn.com/)

<p>写一个函数，求两个整数之和，要求在函数体内不得使用 &ldquo;+&rdquo;、&ldquo;-&rdquo;、&ldquo;*&rdquo;、&ldquo;/&rdquo; 四则运算符号。</p>

<p>&nbsp;</p>

<p><strong>示例:</strong></p>

<pre><strong>输入:</strong> a = 1, b = 1
<strong>输出:</strong> 2</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>a</code>,&nbsp;<code>b</code>&nbsp;均可能是负数或 0</li>
	<li>结果不会溢出 32 位整数</li>
</ul>


## 解法：

做二进制的加法：

`cy = a & b` 是进位。`a & ~b | ~a & b` 是不考虑进位时的结果。将进位左移一位，再次求和。直到没有进位为止。

如果是两个负数相加，那么进位的最高是 `1`，如果 cy 是用补码表示的，再次左移就会出错。因此，将 `cy` 定义为无符号的数。


```c++
class Solution {
public:
    int add(int a, int b) {
        while(b){
            unsigned int cy = a & b;
            a = a & ~b | ~a & b;
            b = cy << 1;
        }
        return a;
    }
};
```