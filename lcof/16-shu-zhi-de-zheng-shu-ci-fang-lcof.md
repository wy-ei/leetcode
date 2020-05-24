## 16. 数值的整数次方

- 难度：Medium
- 题目链接：[https://leetcode-cn.com/problems/shu-zhi-de-zheng-shu-ci-fang-lcof/](https://leetcode-cn.com/problems/shu-zhi-de-zheng-shu-ci-fang-lcof/)


## 题目描述

来源于 [https://leetcode-cn.com/](https://leetcode-cn.com/)

<p>实现函数double Power(double base, int exponent)，求base的exponent次方。不得使用库函数，同时不需要考虑大数问题。</p>

<p>&nbsp;</p>

<p><strong>示例 1:</strong></p>

<pre><strong>输入:</strong> 2.00000, 10
<strong>输出:</strong> 1024.00000
</pre>

<p><strong>示例&nbsp;2:</strong></p>

<pre><strong>输入:</strong> 2.10000, 3
<strong>输出:</strong> 9.26100
</pre>

<p><strong>示例&nbsp;3:</strong></p>

<pre><strong>输入:</strong> 2.00000, -2
<strong>输出:</strong> 0.25000
<strong>解释:</strong> 2<sup>-2</sup> = 1/2<sup>2</sup> = 1/4 = 0.25</pre>

<p>&nbsp;</p>

<p><strong>说明:</strong></p>

<ul>
	<li>-100.0 &lt;&nbsp;<em>x</em>&nbsp;&lt; 100.0</li>
	<li><em>n</em>&nbsp;是 32 位有符号整数，其数值范围是&nbsp;[&minus;2<sup>31</sup>,&nbsp;2<sup>31&nbsp;</sup>&minus; 1] 。</li>
</ul>

<p>注意：本题与主站 50 题相同：<a href="https://leetcode-cn.com/problems/powx-n/">https://leetcode-cn.com/problems/powx-n/</a></p>


## 解法：

不断地进行 `x = x * x` 可以产生 `x^2, x^4, x^8, x^16, ...`。而 `x^(a+b) = x^a * x^b`。另外任何一个 n 都可以写出 `1 2 4 8 16 ...` 中某些数的和，比如 `6 = 2 + 4`，因此 `x^6 = x^2 * x^4`。

因此从最低位开始判断 n 的每一位，当该位是 1 的时候，就在结果中乘上一个 `x`，并在循环中不断更新 `x`。

需要注意的几个问题：

1\. n 为最小的负数的时候，因为需要把 n 转为正数，如果直接取反，整数会溢出。因此需要使用一个无符号的数来存储幂次。另外在取反的时候需要防止溢出。

```cpp
exp = -(n+1);
exp = exp + 1;
```

2\. 当底数为零的时候，指数不能为负数。因为当 n 为正的时候， 0^n = 0，0 取倒数就出错了。


```c++
class Solution {
public:
    double myPow(double x, int n) {
		if(x == 0 && n < 0){
			throw invalid_argument();
		}

        double result = 1;
        unsigned int exp;
        int sign = n < 0 ? -1 : 1;

        if(sign == -1){
            exp = -(n+1);
			exp = exp + 1;
        }else{
			exp = n;
		}

        while(exp){
            if(exp & 1){
                result *= x;
            }
            x = x * x;
            exp >>= 1;
        }

        if(sign == -1){
            result = 1 / result;
        }
        return result;
    }
};
```