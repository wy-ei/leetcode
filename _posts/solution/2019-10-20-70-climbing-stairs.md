---
title: 爬楼梯
qid: 70
tags: [动态规划]
---


- 难度： 简单
- 通过率： 42.7%
- 题目链接：[https://leetcode-cn.com/problems/climbing-stairs](https://leetcode-cn.com/problems/climbing-stairs)


## 题目描述

来源于 [https://leetcode-cn.com/](https://leetcode-cn.com/)

<p>假设你正在爬楼梯。需要 <em>n</em>&nbsp;阶你才能到达楼顶。</p>

<p>每次你可以爬 1 或 2 个台阶。你有多少种不同的方法可以爬到楼顶呢？</p>

<p><strong>注意：</strong>给定 <em>n</em> 是一个正整数。</p>

<p><strong>示例 1：</strong></p>

<pre><strong>输入：</strong> 2
<strong>输出：</strong> 2
<strong>解释：</strong> 有两种方法可以爬到楼顶。
1.  1 阶 + 1 阶
2.  2 阶</pre>

<p><strong>示例 2：</strong></p>

<pre><strong>输入：</strong> 3
<strong>输出：</strong> 3
<strong>解释：</strong> 有三种方法可以爬到楼顶。
1.  1 阶 + 1 阶 + 1 阶
2.  1 阶 + 2 阶
3.  2 阶 + 1 阶
</pre>


## 解法一：自顶向下

青蛙登上 n 级台阶，有两种可能：从 n-1 级台阶跳上来，或者从 n-2 级台阶跳上来。因此，这可能性数量为 F 则：

F(n) = F(n-1) + F(n-2)

这可以写个递归轻松解决，因为其中涉及很多重复计算，可以加个备忘录。

```c++
class Solution {
public:
    int numWays(int n) {
        return num_ways(n);
    }

    int num_ways(int n){
        if(n == 0 || n == 1){
            return 1;
        }

        auto it = cache.find(n);
        if(it != cache.end()){
            return cache[n];
        }

        cache[n] = num_ways(n-1) + num_ways(n-2);
        cache[n] %= 1000000007L;

        return cache[n];
    }
private:
    unordered_map<int, int> cache;
};
```

## 解法二：自底向上

考虑青蛙在第 2 级台阶有几种可能？0->2 和 1->2，不难看出，每一级可能的跳法只和前两级的跳法有关，而且是两者只和。这就和斐波那契数列差不多了，知道初始状态，然后不断累加即可。

可以几乎完全复用前一题的代码，只需要稍微修改启动阶段的初始值即可。

```cpp
class Solution {
public:
    int numWays(int n) {
        const long max_val = 1000000007L;
        if(n == 1) return 1;
        if(n == 1) return 1;
        long a = 1, b = 1;
        for(int i=1; i<n; i++){
            b = a + b;
            a = b - a;
            b %= max_val;
        }
        return b;
    }
};
```