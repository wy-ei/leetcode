## 10- II. 青蛙跳台阶问题

- 难度：Easy
- 题目链接：[https://leetcode-cn.com/problems/qing-wa-tiao-tai-jie-wen-ti-lcof/](https://leetcode-cn.com/problems/qing-wa-tiao-tai-jie-wen-ti-lcof/)


## 题目描述

来源于 [https://leetcode-cn.com/](https://leetcode-cn.com/)

<p>一只青蛙一次可以跳上1级台阶，也可以跳上2级台阶。求该青蛙跳上一个 <code>n</code>&nbsp;级的台阶总共有多少种跳法。</p>

<p>答案需要取模 1e9+7（1000000007），如计算初始结果为：1000000008，请返回 1。</p>

<p><strong>示例 1：</strong></p>

<pre><strong>输入：</strong>n = 2
<strong>输出：</strong>2
</pre>

<p><strong>示例 2：</strong></p>

<pre><strong>输入：</strong>n = 7
<strong>输出：</strong>21
</pre>

<p><strong>提示：</strong></p>

<ul>
	<li><code>0 &lt;= n &lt;= 100</code></li>
</ul>

<p>注意：本题与主站 70 题相同：<a href="https://leetcode-cn.com/problems/climbing-stairs/">https://leetcode-cn.com/problems/climbing-stairs/</a></p>

<p>&nbsp;</p>


## 解法一：自顶向下

青蛙登上 n 级台阶，有两种可能：从 n-1 级台阶跳上来，或者从 n-2 级台阶跳上来。因此，这可能性为 F 则：

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