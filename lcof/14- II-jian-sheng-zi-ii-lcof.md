## 14- II. 剪绳子 II

- 难度：Medium
- 题目链接：[https://leetcode-cn.com/problems/jian-sheng-zi-ii-lcof/](https://leetcode-cn.com/problems/jian-sheng-zi-ii-lcof/)


## 题目描述

来源于 [https://leetcode-cn.com/](https://leetcode-cn.com/)

<p>给你一根长度为 <code>n</code> 的绳子，请把绳子剪成整数长度的 <code>m</code> 段（m、n都是整数，n&gt;1并且m&gt;1），每段绳子的长度记为 <code>k[0],k[1]...k[m]</code> 。请问 <code>k[0]*k[1]*...*k[m]</code> 可能的最大乘积是多少？例如，当绳子的长度是8时，我们把它剪成长度分别为2、3、3的三段，此时得到的最大乘积是18。</p>

<p>答案需要取模 1e9+7（1000000007），如计算初始结果为：1000000008，请返回 1。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre><strong>输入: </strong>2
<strong>输出: </strong>1
<strong>解释: </strong>2 = 1 + 1, 1 &times; 1 = 1</pre>

<p><strong>示例&nbsp;2:</strong></p>

<pre><strong>输入: </strong>10
<strong>输出: </strong>36
<strong>解释: </strong>10 = 3 + 3 + 4, 3 &times;&nbsp;3 &times;&nbsp;4 = 36</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>2 &lt;= n &lt;= 1000</code></li>
</ul>

<p>注意：本题与主站 343 题相同：<a href="https://leetcode-cn.com/problems/integer-break/">https://leetcode-cn.com/problems/integer-break/</a></p>


## 解法：

这里需要在累乘的时候保持结果不超过一个数，因此在循环中不断判断结果是否大于这个数，一旦大于，就取余。即使当前结果不大于 1000000007，乘上 3 之后，得到的结果有可能达到 30 亿，而 32 位的 int 最大存储 21 亿左右。但是无符号的 int 可以存储大小 42 亿多的数。因此，使用无符号的 int 即可。

```c++
class Solution {
public:
    int cuttingRope(int n) {
		if(n == 2) return 1;
		if(n == 3) return 2;

		int num_3 = n / 3;
		int num_2 = 0;
		if(n % 3 == 2){
			num_2 = 1;
		}else if(n % 3 == 1){
			num_3 -= 1;
			num_2 = 2;
		}

		unsigned int ret = 1;
		for(int i=0;i<num_3;i++){
			ret *= 3;
			while(ret >= 1000000007){
				ret -= 1000000007;
			}
		}
		for(int i=0;i<num_2;i++){
			ret *= 2;
			while(ret >= 1000000007){
				ret -= 1000000007;
			}
		}
		return ret;
    }
};
```