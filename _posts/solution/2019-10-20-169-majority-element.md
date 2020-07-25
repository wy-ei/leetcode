---
title: 多数元素
qid: 169
tags: [位运算,数组,分治算法]
---


- 难度： 简单
- 通过率： 50.7%
- 题目链接：[https://leetcode-cn.com/problems/majority-element](https://leetcode-cn.com/problems/majority-element)


## 题目描述

来源于 [https://leetcode-cn.com/](https://leetcode-cn.com/)

<p>给定一个大小为 <em>n </em>的数组，找到其中的众数。众数是指在数组中出现次数<strong>大于</strong>&nbsp;<code>&lfloor; n/2 &rfloor;</code>&nbsp;的元素。</p>

<p>你可以假设数组是非空的，并且给定的数组总是存在众数。</p>

<p><strong>示例&nbsp;1:</strong></p>

<pre><strong>输入:</strong> [3,2,3]
<strong>输出:</strong> 3</pre>

<p><strong>示例&nbsp;2:</strong></p>

<pre><strong>输入:</strong> [2,2,1,1,1,2,2]
<strong>输出:</strong> 2
</pre>


## 解法：

这道题，最直白的解法是使用一个 map 来记录各个数字出现的次数，最后取出现次数最多的作为解。但这个方法需要消耗额外的空间，不是最优。下面是最优解法：

我们做这样的想象，现在有来自不同阵营的多支部队，他们互为敌人。每个士兵都容不得敌人，宁愿与敌人同归于尽。可以想象，如果某个阵营的士兵数量超过所有阵营士兵总数的一半，该阵营士兵一换一带走一个其他阵营的，最终剩下的就是该阵营的士兵了，该阵营就获胜了。

这和本题有什么关系呢？且看下面的故事：

现在要打仗了，所有士兵依次进入战场，如果战场上有其他阵营的士兵，他就与其中一个同归于尽。否则，他就留在战场上。容易想象，战场上要么没有人，要么是同一阵营的。所有士兵都进入战场后，最终战场上剩下的只会是同一阵营的，而该阵营就是人数过半的那个。

我们要模拟这个过程，找到那个获胜的阵营。数组中每个元素就是士兵，元素的值，就是这个士兵所属阵营。

```cpp
class Solution {
public:
    int majorityElement(vector<int> nums) {
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

**补充说明**

如果可以保证某个阵营的人数过半，那么最后留下的就一定是这个阵营的士兵。但如果没有任何一个阵营人数过半，那么某个阵营可以猫在最后，在其他阵营都厮杀结束后进入战场，坐收渔翁之利。

因此，如果不存出现过半的数，上面的算法是错误的，需要加一个检验判断一下 win 是否出现了一般以上。