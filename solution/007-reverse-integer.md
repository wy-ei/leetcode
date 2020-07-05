## 7. Reverse Integer

- 难度： 简单
- 通过率： 24.9%
- 题目链接：[https://leetcode.com/problems/reverse-integer](https://leetcode.com/problems/reverse-integer)


## 题目描述

来源于 [https://leetcode-cn.com/](https://leetcode-cn.com/)

<p>给出一个 32 位的有符号整数，你需要将这个整数中每位上的数字进行反转。</p>

<p><strong>示例&nbsp;1:</strong></p>

<pre><strong>输入:</strong> 123
<strong>输出:</strong> 321
</pre>

<p><strong>&nbsp;示例 2:</strong></p>

<pre><strong>输入:</strong> -123
<strong>输出:</strong> -321
</pre>

<p><strong>示例 3:</strong></p>

<pre><strong>输入:</strong> 120
<strong>输出:</strong> 21
</pre>

<p><strong>注意:</strong></p>

<p>假设我们的环境只能存储得下 32 位的有符号整数，则其数值范围为&nbsp;[&minus;2<sup>31</sup>,&nbsp; 2<sup>31&nbsp;</sup>&minus; 1]。请根据这个假设，如果反转后整数溢出那么就返回 0。</p>



## 解法

这题很容易，但是因为不同的语言中负数取余的行为不同，这里干脆先转换为正数，再做其他处理。

```c++
class Solution {
public:
    int reverse(int x) {
        long long n = x;
        long long r = 0;
        n = (x >= 0) ? n : -n;

        while (n) {
            r = r * 10 + n % 10;
            n /= 10;
        }
        r = (x >= 0) ? r : -r;

        if (x > 0 && r > INT_MAX) {
            return 0;
        }
        if (x < 0 && r < INT_MIN) {
            return 0;
        }
        return r;
    }
};
```
