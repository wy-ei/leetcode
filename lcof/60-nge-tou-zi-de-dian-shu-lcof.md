## 60. n个骰子的点数

- 难度：Easy
- 题目链接：[https://leetcode-cn.com/problems/nge-tou-zi-de-dian-shu-lcof/](https://leetcode-cn.com/problems/nge-tou-zi-de-dian-shu-lcof/)


## 题目描述

来源于 [https://leetcode-cn.com/](https://leetcode-cn.com/)

<p>把n个骰子扔在地上，所有骰子朝上一面的点数之和为s。输入n，打印出s的所有可能的值出现的概率。</p>

<p>&nbsp;</p>

<p>你需要用一个浮点数数组返回答案，其中第 i 个元素代表这 n 个骰子所能掷出的点数集合中第 i 小的那个的概率。</p>

<p>&nbsp;</p>

<p><strong>示例 1:</strong></p>

<pre><strong>输入:</strong> 1
<strong>输出:</strong> [0.16667,0.16667,0.16667,0.16667,0.16667,0.16667]
</pre>

<p><strong>示例&nbsp;2:</strong></p>

<pre><strong>输入:</strong> 2
<strong>输出:</strong> [0.02778,0.05556,0.08333,0.11111,0.13889,0.16667,0.13889,0.11111,0.08333,0.05556,0.02778]</pre>

<p>&nbsp;</p>

<p><strong>限制：</strong></p>

<p><code>1 &lt;= n &lt;= 11</code></p>


## 解法：

本质上是求 n 个骰子的和为 s 时，一共有多少种可能。每种可能的概率是 `(1/6)^n`，所以知道了可能的数量，就可以算出概率。

求 n 个骰子和为 `s` 的数量时，可以把 `n-1` 个骰子和为 `s-1, s-2, s-3, ..., s-6` 的可能累加起来。最底层，1 个骰子和为 `1 2 3 4 5 6` 时的可能数都是 `1`。以此 1 个骰子作为初始条件，自底向上地计算，`n_touzi=2,3,4,...,n` 时，`s` 取 `n~6*n` 时的可能数。

最终能够得到 `n` 个骰子时 `s` 的不同取值下的可能数，至此概率就可以求出来了。

```c++
class Solution {
public:
    vector<double> twoSum(int n) {
        unordered_map<int, unordered_map<int, int>> dp;

        for(int s=1;s<=6;s++){
            dp[1][s] = 1;
        }

        for(int n_touzi = 2; n_touzi <= n; n_touzi++){
            for(int s = n_touzi; s <= n_touzi * 6; s++){
                for(int i = 1;i<=6;i++){
                    if(dp[n_touzi-1].find(s-i) != dp[n_touzi-1].end()){
                        dp[n_touzi][s] += dp[n_touzi-1][s-i];
                    }
                }
            }
        }

        double p = pow(1.0/6, n);

        vector<double> ret;
        for(int s = n; s <= n * 6; s++){
            ret.push_back(dp[n][s] * p);
        }

        return ret;
    }
};
```