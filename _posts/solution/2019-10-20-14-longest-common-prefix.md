---
title: 最长公共前缀
qid: 14
tags: [字符串]
---


- 难度： 简单
- 通过率： 32.6%
- 题目链接：[https://leetcode-cn.com/problems/longest-common-prefix](https://leetcode-cn.com/problems/longest-common-prefix)


## 题目描述

来源于 [https://leetcode-cn.com/](https://leetcode-cn.com/)

<p>编写一个函数来查找字符串数组中的最长公共前缀。</p>

<p>如果不存在公共前缀，返回空字符串&nbsp;<code>&quot;&quot;</code>。</p>

<p><strong>示例&nbsp;1:</strong></p>

<pre><strong>输入: </strong>[&quot;flower&quot;,&quot;flow&quot;,&quot;flight&quot;]
<strong>输出:</strong> &quot;fl&quot;
</pre>

<p><strong>示例&nbsp;2:</strong></p>

<pre><strong>输入: </strong>[&quot;dog&quot;,&quot;racecar&quot;,&quot;car&quot;]
<strong>输出:</strong> &quot;&quot;
<strong>解释:</strong> 输入不存在公共前缀。
</pre>

<p><strong>说明:</strong></p>

<p>所有输入只包含小写字母&nbsp;<code>a-z</code>&nbsp;。</p>


## 解法：

```c++
class Solution {
public:
    string longestCommonPrefix(vector<string> &strs) {
        if (strs.empty()) return "";

        string prefix;
        for (size_t i = 0; i < strs.front().size(); i++) {
            char ch = strs.front()[i];
            for (auto& s: strs) {
                if (i == s.size() || s[i] != ch) {
                    return prefix;
                }
            }
            prefix += ch;
        }
        return prefix;
    }
};
```