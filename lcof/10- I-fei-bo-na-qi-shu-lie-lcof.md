## 10- I. 斐波那契数列

- 难度：Easy
- 题目链接：[https://leetcode-cn.com/problems/fei-bo-na-qi-shu-lie-lcof/](https://leetcode-cn.com/problems/fei-bo-na-qi-shu-lie-lcof/)


## 题目描述

来源于 [https://leetcode-cn.com/](https://leetcode-cn.com/)

<p>写一个函数，输入 <code>n</code> ，求斐波那契（Fibonacci）数列的第 <code>n</code> 项。斐波那契数列的定义如下：</p>

<pre>F(0) = 0,&nbsp; &nbsp;F(1)&nbsp;= 1
F(N) = F(N - 1) + F(N - 2), 其中 N &gt; 1.</pre>

<p>斐波那契数列由 0 和 1 开始，之后的斐波那契数就是由之前的两数相加而得出。</p>

<p>答案需要取模 1e9+7（1000000007），如计算初始结果为：1000000008，请返回 1。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre><strong>输入：</strong>n = 2
<strong>输出：</strong>1
</pre>

<p><strong>示例 2：</strong></p>

<pre><strong>输入：</strong>n = 5
<strong>输出：</strong>5
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>0 &lt;= n &lt;= 100</code></li>
</ul>

<p>注意：本题与主站 509 题相同：<a href="https://leetcode-cn.com/problems/fibonacci-number/">https://leetcode-cn.com/problems/fibonacci-number/</a></p>


## 解法：

常规解法，迭代即可，需要注意的就是迭代的次数。设 a 和 b 是斐波那契数列中连续的两个值，在迭代中不断更新 a 和 b 就可以了。更新时，可以使用临时变量存下 b 的值，也可以采用下面代码中的写法。

由于斐波那契数列增长的超级快，题目中提到要取余保证数值不溢出。可以在更新 b 的值后，判断它是否大于或等于该最大值，必要的时候减去该最大值，这种方法比取余速度更快。

```cpp
class Solution {
public:
    int fib(int n) {
		const long max_val = 1000000007L;
        if(n == 0) return 0;
        if(n == 1) return 1;
        long a = 0, b = 1;
        for(int i=1; i<n; i++){
            b = a + b;
            a = b - a;
            b %= max_val;
        }
        return b;
    }
};
```

如果需要大量地调用该方法，自然是要加一个缓存。