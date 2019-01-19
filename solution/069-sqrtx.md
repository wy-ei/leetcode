## 69. Sqrt(x)

- 难度： 简单
- 通过率： 30.1%
- 题目链接：[https://leetcode.com/problems/sqrtx](https://leetcode.com/problems/sqrtx)


### 题目描述

来源于 [https://leetcode-cn.com/](https://leetcode-cn.com/)

<p>实现&nbsp;<code>int sqrt(int x)</code>&nbsp;函数。</p>

<p>计算并返回&nbsp;<em>x</em>&nbsp;的平方根，其中&nbsp;<em>x </em>是非负整数。</p>

<p>由于返回类型是整数，结果只保留整数的部分，小数部分将被舍去。</p>

<p><strong>示例 1:</strong></p>

<pre><strong>输入:</strong> 4
<strong>输出:</strong> 2
</pre>

<p><strong>示例 2:</strong></p>

<pre><strong>输入:</strong> 8
<strong>输出:</strong> 2
<strong>说明:</strong> 8 的平方根是 2.82842..., 
&nbsp;    由于返回类型是整数，小数部分将被舍去。
</pre>


### 解法：

采用牛顿法来解，解释见 [使用牛顿迭代法求平方根](https://github.com/wy-ei/notebook/issues/50)

```python
import math
class Solution:
    def mySqrt(self, n):
        """
        :type x: int
        :rtype: int
        """
        if n <= 1:
            return n
        
        e = 1e-15
        
        x = n
        x_next = (x + n / x) / 2
        
        while abs(x_next - x) > e:
            x = x_next
            x_next = (x + n / x) / 2
        
        return math.floor(x)
```