---
title: 分割回文串 II
qid: 132
tags: [动态规划]
---


- 难度： 困难
- 通过率： 26.3%
- 题目链接：[https://leetcode-cn.com/problems/palindrome-partitioning-ii](https://leetcode-cn.com/problems/palindrome-partitioning-ii)


## 题目描述

来源于 [https://leetcode-cn.com/](https://leetcode-cn.com/)

<p>给定一个字符串 <em>s</em>，将 <em>s</em> 分割成一些子串，使每个子串都是回文串。</p>

<p>返回符合要求的最少分割次数。</p>

<p><strong>示例:</strong></p>

<pre><strong>输入:</strong>&nbsp;&quot;aab&quot;
<strong>输出:</strong> 1
<strong>解释: </strong>进行一次分割就可将&nbsp;<em>s </em>分割成 [&quot;aa&quot;,&quot;b&quot;] 这样两个回文子串。
</pre>


## 解法：

使用动态规划，记录下在各个位置之前需要进行的划分次数。

`dp[i]` 就表示前 i 个字符需要划分的次数。初始状态下 `dp = [-1, 0, 1, 2, ...]`

对于回文串 `s[start:end]`，`dp[end+1] = min(dp[end+1], dp[start] + 1)`

取 `dp[0] = -1` 可以简化状态方程的更新过程。


```python
class Solution:
    def minCut(self, s: str) -> List[List[str]]:
        dp = [i for i in range(-1, len(s))]
        for end in range(len(s)):
            for start in range(end+1):
                if s[start:end+1] == s[start:end+1][::-1]:
                    dp[end+1] = min(dp[end+1], dp[start]+1)
                    
        return dp[-1]
```