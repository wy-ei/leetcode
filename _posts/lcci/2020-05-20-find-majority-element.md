---
title: 主要元素
qid: 17.10
tags: [位运算,数组,分治算法]
---


- 难度：Easy
- 题目链接：[https://leetcode-cn.com/problems/find-majority-element-lcci/](https://leetcode-cn.com/problems/find-majority-element-lcci/)


## 题目描述

来源于 [https://leetcode-cn.com/](https://leetcode-cn.com/)

<p>数组中占比超过一半的元素称之为主要元素。给定一个<strong>整数</strong>数组，找到它的主要元素。若没有，返回-1。</p>

<p><strong>示例 1：</strong></p>

<pre><strong>输入：</strong>[1,2,5,9,5,9,5,5,5]
<strong>输出：</strong>5</pre>

<p>&nbsp;</p>

<p><strong>示例 2：</strong></p>

<pre><strong>输入：</strong>[3,2]
<strong>输出：</strong>-1</pre>

<p>&nbsp;</p>

<p><strong>示例 3：</strong></p>

<pre><strong>输入：</strong>[2,2,1,1,1,2,2]
<strong>输出：</strong>2</pre>

<p>&nbsp;</p>

<p><strong>说明：</strong><br>
你有办法在时间复杂度为 O(N)，空间复杂度为 O(1) 内完成吗？</p>


## 解法：


我们做这样的想象，一大群战士分为多个阵营，每个战士都容不下其他阵营的，都情愿牺牲自己带走一个其他阵营的。可以想象，某个阵营的人数如果超过一半，该阵营的人一换一带走其他阵营的，剩下的就是该阵营的人了，该阵营就获胜了。


现在要打仗了，所有人依次进入战场，如果战场上有其他阵营的士兵，他就和其他一个同归于尽。否则，他就留在战场上。容易想象，战场上要么没有人，要么是同一阵营的。所有战士都进入战场后，最终战场上剩下的只会是同一阵营的，而该阵营就是人数过半的那个阵营。

我们要模拟这个过程，找到那个获胜的阵营。数组中每个元素就是战士，元素的值，就是这个战士所属阵营。


```cpp
class Solution {
public:
    int majorityElement(vector&lt;int&gt; nums) {
        int count = 0;
        int win;

        for(int n: nums){
            // 战场上没人
            if(count == 0){
                win = n;
                count = 1;
            }else{
                // 同一阵营
                if(win == n){
                    count++;
                }
                // 不同阵营
                else{
                    count--;
                }
            }
        }
        
        return win;
    }
};
```

### 补充说明

如果可以保证某个阵营的人数过半，那么最后留下的就一定是这个阵营的战士。但如果没有任何一个阵营人数过半，那么某个阵营可以猫在最后，他们可以猫在最后进入战场，快速打扫战场，然后取得胜利。

因此，如果不存出现过半的数，上面的算法是错误的。