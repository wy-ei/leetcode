---
title: 最长回文子串
qid: 5
tags: [字符串,动态规划]
---


- 难度： 中等
- 通过率： 25.9%
- 题目链接：[https://leetcode-cn.com/problems/longest-palindromic-substring](https://leetcode-cn.com/problems/longest-palindromic-substring)


## 题目描述

来源于 [https://leetcode-cn.com/](https://leetcode-cn.com/)

<p>给定一个字符串 <code>s</code>，找到 <code>s</code> 中最长的回文子串。你可以假设&nbsp;<code>s</code> 的最大长度为 1000。</p>

<p><strong>示例 1：</strong></p>

<pre><strong>输入:</strong> &quot;babad&quot;
<strong>输出:</strong> &quot;bab&quot;
<strong>注意:</strong> &quot;aba&quot; 也是一个有效答案。
</pre>

<p><strong>示例 2：</strong></p>

<pre><strong>输入:</strong> &quot;cbbd&quot;
<strong>输出:</strong> &quot;bb&quot;
</pre>



## 解法一：中心扩散法

以字符串的每个位置为中心，向两边扩张，以此得到，当两边的字符串不同的时候，就停止。

```cpp
class Solution {
public:
    string longestPalindrome(string s) {
        if(s.size() < 2) return s;

        int max_len = 0;
        int start = 0;
        for(int i = 0;i<s.size();i++) {
            int len1 = expand(s, i - 1, i + 1);
            int len2 = expand(s, i, i + 1);
            int len = max(len1, len2);
            if (len > max_len) {
                start = i - (len - 1) / 2;
                max_len = len;
            }
        }
        return s.substr(start, max_len);
    }

    int expand(const string &s, int lo, int hi){
        while(lo >= 0 && hi < s.size() && s[lo] == s[hi]){
            --lo;
            ++hi;
        }
        return hi - lo - 1;
    }
};
```

## 解法二：动态规划

如果已知 `a[i..j]` 为回文串，那么如果 `a[i-1] == a[j+1]` 则 `a[i-1..j+1]` 为回文子串。

用 `f(i,j)` 表示 `a[i:j]` 是否为回文串，那么：

- `f(i, i) = true`
- `f(i+1, j+1) = f(i, j) && s[i-1] == s[j+1]`

使用动态规划，需要存储空间为 `O(n^2)`，需要的计算时间为 `O(n^2)` 没有任何优势。

```c++
class Solution {
public:
    string longestPalindrome(string &s) {
        if (s.empty()) return s;
        const int n = s.size();
        bool dp[n][n];
        fill_n(&dp[0][0], n * n, false);

        size_t max_len = 1, start = 0;

        for (size_t i = 0; i < n; i++) {
            dp[i][i] = true;
            for (size_t j = i; j < n; j++) { // [i, j]
                f[i][j] = (s[i] == s[j]) && ( j - i <= 1 || f[i + 1][j - 1]);
                size_t len = i - j + 1;
                if (f[j][i] && max_len < len) {
                    max_len = len;
                    start = j;
                }
            }
        }

        return s.substr(start, max_len);
    }
};
```