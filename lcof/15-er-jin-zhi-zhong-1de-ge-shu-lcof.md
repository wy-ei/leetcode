## 15. 二进制中1的个数

- 难度：Easy
- 题目链接：[https://leetcode-cn.com/problems/er-jin-zhi-zhong-1de-ge-shu-lcof/](https://leetcode-cn.com/problems/er-jin-zhi-zhong-1de-ge-shu-lcof/)


## 题目描述

来源于 [https://leetcode-cn.com/](https://leetcode-cn.com/)

<p>请实现一个函数，输入一个整数，输出该数二进制表示中 1 的个数。例如，把 9&nbsp;表示成二进制是 1001，有 2 位是 1。因此，如果输入 9，则该函数输出 2。</p>

<p><strong>示例 1：</strong></p>

<pre><strong>输入：</strong>00000000000000000000000000001011
<strong>输出：</strong>3
<strong>解释：</strong>输入的二进制串 <code><strong>00000000000000000000000000001011</strong>&nbsp;中，共有三位为 &#39;1&#39;。</code>
</pre>

<p><strong>示例 2：</strong></p>

<pre><strong>输入：</strong>00000000000000000000000010000000
<strong>输出：</strong>1
<strong>解释：</strong>输入的二进制串 <strong>00000000000000000000000010000000</strong>&nbsp;中，共有一位为 &#39;1&#39;。
</pre>

<p><strong>示例 3：</strong></p>

<pre><strong>输入：</strong>11111111111111111111111111111101
<strong>输出：</strong>31
<strong>解释：</strong>输入的二进制串 <strong>11111111111111111111111111111101</strong> 中，共有 31 位为 &#39;1&#39;。</pre>

<p>&nbsp;</p>

<p>注意：本题与主站 191 题相同：<a href="https://leetcode-cn.com/problems/number-of-1-bits/">https://leetcode-cn.com/problems/number-of-1-bits/</a></p>


## 解法：

一种思路是直接遍历该数的每一个 bit，统计 1 出现的次数。我们不能把 n 做循环右移，然后当它为 0 的时候停止。因为如果 n 是负数，那么右移不会得到 0。采用这种方法时候，可以限定移动的次数。

另外一个方法就是把 1 每次左移一位，然后去检查 n 中的各个位，检查完了之后可以把当前 bit 置为 0，当 n 为 0 的时候，就可以停止遍历了。


```c++
class Solution {
public:
     int  NumberOf1(int n) {
        int num = 0;
        unsigned int m = 1;
         while(n){
             if(n & m){
                 num += 1;
             }
             n = n & ~m;
             m = m << 1;
         }
         return num;
     }
};
```

上面的解法如果 n 的最高位是 1，其他都是 0，那么也需要 32 次循环。但是下面的方法就不一样了，它只需要一次循环，因为该方法每次都可以消除掉一个 1，一旦所有 1 都被置为 0 了之后，循环就停止了。

每次消除最低位的 1，做法很巧妙 `n = n & (n-1)`，考虑 n = 8。

```
8 -> 1 0 0 0
7 -> 0 1 1 1
```

n - 1 在二进制表示中呈现出来的规律是：把最低位的 1 置 0，其后的所有 0 置为 1。两者做按位与之后，就消除了最低位的 1。

在循环中反复消除最低位的 1，当 n 为 0 时，循环退出。1 的个数，自然就是循环的次数。


```c++
class Solution {
public:
     int NumberOf1(int n) {
         int num = 0;
         while(n){
             n = n & (n-1);
             num += 1;
         }
         return num;
     }
};
```