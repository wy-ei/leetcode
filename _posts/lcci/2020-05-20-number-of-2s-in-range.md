---
title: 2出现的次数
qid: 17.06
tags: [数学,动态规划]
---


- 难度：Medium
- 题目链接：[https://leetcode-cn.com/problems/number-of-2s-in-range-lcci/](https://leetcode-cn.com/problems/number-of-2s-in-range-lcci/)


## 题目描述

来源于 [https://leetcode-cn.com/](https://leetcode-cn.com/)

<p>编写一个方法，计算从 0 到 n (含 n) 中数字 2 出现的次数。</p>

<p><strong>示例:</strong></p>

<pre><strong>输入: </strong>25
<strong>输出: </strong>9
<strong>解释: </strong>(2, 12, 20, 21, 22, 23, 24, 25)(注意 22 应该算作两次)</pre>

<p>提示：</p>

<ul>
	<li><code>n &lt;= 10^9</code></li>
</ul>


## 解法：

把每一位上的数设置为 2 之后，看其他所有位变化的可能数。

```c++
class Solution {
public:
    int numberOf2sInRange(int num) {
        int low = 0, high = num;
        int n = 0;
        int count = 0, i = 0;
        
        while(high){
            int base = pow(10, i);
            n = high % 10;
            low = num - high * base;
            high /= 10;

            if(n < 2){
                count += high * base;
            }else if(n == 2){
                count += high * base + low + 1;
            }else if(n > 2){
                count += (high+1) * base;
            }
            i++;
        }

        return count;
    }
};
```