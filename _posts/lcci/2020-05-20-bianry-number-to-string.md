---
title: 二进制数转字符串
qid: 05.02
tags: [字符串]
---


- 难度：Medium
- 题目链接：[https://leetcode-cn.com/problems/bianry-number-to-string-lcci/](https://leetcode-cn.com/problems/bianry-number-to-string-lcci/)


## 题目描述

来源于 [https://leetcode-cn.com/](https://leetcode-cn.com/)

<p>二进制数转字符串。给定一个介于0和1之间的实数（如0.72），类型为double，打印它的二进制表达式。如果该数字不在0和1之间，<strong>或者</strong>无法精确地用32位以内的二进制表示，则打印&ldquo;ERROR&rdquo;。</p>

<p><strong>示例1:</strong></p>

<pre><strong> 输入</strong>：0.625
<strong> 输出</strong>：&quot;0.101&quot;
</pre>

<p><strong>示例2:</strong></p>

<pre><strong> 输入</strong>：0.1
<strong> 输出</strong>：&quot;ERROR&quot;
<strong> 提示</strong>：0.1无法被二进制准确表示
</pre>

<p><strong>提示：</strong></p>

<ol>
	<li>32位包括输出中的&quot;0.&quot;这两位。</li>
</ol>


## 解法：

二进制的 `0.101` 表示的是 `0.625`，浮点中的个位代表的是 `2^-i`，比如 `0.625` 是按如下方式构成的：

```
0.625 = 0.5 + 0.25 + 0.125
```

要确定小数点后各位的二进制表示是 1 还是 0，可以判断浮点数是否大于 `0.5`，如果大于 `0.5`，说明浮点数的最高位上为 `1`。然后减去 `0.5`，再判断是否大于 `0.25`，接下来判断是否大于 `0.125`，以此类推。

```c++
class Solution {
public:
    string printBin(double num) {
        if(num >= 1 || num < 0){
            return "ERROR";
        }
        string ret = "0.";
        double n=1;
        int i = 0;
        while(++i <= 32 && num > 0){
            n /= 2;
            if(num >= n){
                ret += '1';
                num -= n;
            }else{
                ret += '0';
            }
        }
        if(i > 32) return "ERROR";
        return ret;
    }
};
```


也可以用浮点数不断乘以 2，如果结果大于 1，说明浮点数大于 0.5。此时把它减去 1，然后再乘以 2，原来 0.25 的部分就被扩大了 4 倍，判断它是否大于 1，就能知道是否包含 0.25 这个成分。


```c++
class Solution {
public:
    string printBin(double num) {
        if(num >= 1 || num < 0){
            return "ERROR";
        }
        string ret = "0.";
        int i=0;
        while(++i <= 32 && num > 0){
            double n = num * 2;
            if(n >= 1){
                ret += '1';
                num = n - 1;
            }else{
                ret += '0';
                num = n;
            }
        }
        if(i > 32) return "ERROR";
        return ret;
    }
};
```