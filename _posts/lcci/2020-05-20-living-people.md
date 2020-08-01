---
title: 生存人数
qid: 16.10
tags: [数组]
---


- 难度：Medium
- 题目链接：[https://leetcode-cn.com/problems/living-people-lcci/](https://leetcode-cn.com/problems/living-people-lcci/)


## 题目描述

来源于 [https://leetcode-cn.com/](https://leetcode-cn.com/)

<p>给定N个人的出生年份和死亡年份，第<code>i</code>个人的出生年份为<code>birth[i]</code>，死亡年份为<code>death[i]</code>，实现一个方法以计算生存人数最多的年份。</p>
<p>你可以假设所有人都出生于1900年至2000年（含1900和2000）之间。如果一个人在某一年的任意时期都处于生存状态，那么他们应该被纳入那一年的统计中。例如，生于1908年、死于1909年的人应当被列入1908年和1909年的计数。</p>
<p>如果有多个年份生存人数相同且均为最大值，输出其中最小的年份。</p>
<p><strong>示例：</strong></p>
<pre><strong>输入：</strong>
birth = {1900, 1901, 1950}
death = {1948, 1951, 2000}
<strong>输出：</strong> 1901
</pre>
<p><strong>提示：</strong></p>
<ul>
<li><code>0 < birth.length == death.length <= 10000</code></li>
<li><code>birth[i] <= death[i]</code></li>
</ul>


## 解法：

如果能记录下每年人口的增量，那么每一年的人口数量，就可以通过累加增长量得到。因此，对于每一个出生和死亡对，可以在出生的那一年 +1，表示当年人口增量 +1，可以在死亡的后一年 -1，表示这年人口增长量 -1。然后按照份遍历这个增量记录，就可以得到各年的人口数量了。

```c++
class Solution {
public:
    int maxAliveYear(vector<int>& birth, vector<int>& death) {
        vector<int> increase_nums(102, 0);

        for(int i=0;i<birth.size();i++){
            increase_nums[birth[i] - 1900]++;
            increase_nums[death[i] - 1900 + 1]--;
        }

        int max_alive_num = 0;
        int alive_num = 0;
        int year = 0;
        for(int i=0;i<increase_nums.size();i++){
            alive_num += increase_nums[i];
            if(alive_num > max_alive_num){
                max_alive_num = alive_num;
                year = i + 1900;
            }
        }
        return year;
    }
};
```