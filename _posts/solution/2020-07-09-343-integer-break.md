---
title: 整数拆分
qid: 343
tag: [数学, 动态规划]
---

- 难度： 中等
- 通过率： 47.1%
- 题目链接：[https://leetcode-cn.com/problems/integer-break](https://leetcode-cn.com/problems/integer-break)


## 题目描述

来源于 [https://leetcode-cn.com/](https://leetcode-cn.com/)

<p>给定一个正整数&nbsp;<em>n</em>，将其拆分为<strong>至少</strong>两个正整数的和，并使这些整数的乘积最大化。 返回你可以获得的最大乘积。</p>

<p><strong>示例 1:</strong></p>

<pre><strong>输入: </strong>2
<strong>输出: </strong>1
<strong>解释: </strong>2 = 1 + 1, 1 &times; 1 = 1。</pre>

<p><strong>示例&nbsp;2:</strong></p>

<pre><strong>输入: </strong>10
<strong>输出: </strong>36
<strong>解释: </strong>10 = 3 + 3 + 4, 3 &times;&nbsp;3 &times;&nbsp;4 = 36。</pre>

<p><strong>说明: </strong>你可以假设&nbsp;<em>n&nbsp;</em>不小于 2 且不大于 58。</p>


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
            ret %= 1000000007;
		}
		for(int i=0;i<num_2;i++){
			ret *= 2;
            ret %= 1000000007;
		}
		return ret;
    }
};
```