## 44. 数字序列中某一位的数字

- 难度：Medium
- 题目链接：[https://leetcode-cn.com/problems/shu-zi-xu-lie-zhong-mou-yi-wei-de-shu-zi-lcof/](https://leetcode-cn.com/problems/shu-zi-xu-lie-zhong-mou-yi-wei-de-shu-zi-lcof/)


## 题目描述

来源于 [https://leetcode-cn.com/](https://leetcode-cn.com/)

<p>数字以0123456789101112131415&hellip;的格式序列化到一个字符序列中。在这个序列中，第5位（从下标0开始计数）是5，第13位是1，第19位是4，等等。</p>

<p>请写一个函数，求任意第n位对应的数字。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre><strong>输入：</strong>n = 3
<strong>输出：</strong>3
</pre>

<p><strong>示例 2：</strong></p>

<pre><strong>输入：</strong>n = 11
<strong>输出：</strong>0</pre>

<p>&nbsp;</p>

<p><strong>限制：</strong></p>

<ul>
	<li><code>0 &lt;= n &lt;&nbsp;2^31</code></li>
</ul>

<p>注意：本题与主站 400 题相同：<a href="https://leetcode-cn.com/problems/nth-digit/">https://leetcode-cn.com/problems/nth-digit/</a></p>


## 解法：

```c++
class Solution {
public:
    int findNthDigit(int n) {
        if(n < 10) return n;

        int width = 0;
        int count = 9;
        int i = 1;
        int len = 0;
        while(i + len <= n){
            i += len;
            width += 1;
            
            // 直接执行 len = count * width 会在最后一次
            // 循环的时候发生溢出，因此在这里先做判断
            if(count > (n - i) / width){
                break;
            }
            
            len = count * width;
            count *= 10;

        }
        int num = pow(10, width-1) + (n - i) / width;
        int m = (n - i) % width;
        for(int k=width-1;k>m;k--){
            num = num / 10;
        }
        return num % 10;
    }
};
```