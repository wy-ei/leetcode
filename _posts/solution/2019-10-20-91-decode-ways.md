---
title: 解码方法
qid: 91
tags: [字符串,动态规划]
---


- 难度： 中等
- 通过率： 21.5%
- 题目链接：[https://leetcode-cn.com/problems/decode-ways](https://leetcode-cn.com/problems/decode-ways)


## 题目描述

来源于 [https://leetcode-cn.com/](https://leetcode-cn.com/)

<p>一条包含字母&nbsp;<code>A-Z</code> 的消息通过以下方式进行了编码：</p>

<pre>&#39;A&#39; -&gt; 1
&#39;B&#39; -&gt; 2
...
&#39;Z&#39; -&gt; 26
</pre>

<p>给定一个只包含数字的<strong>非空</strong>字符串，请计算解码方法的总数。</p>

<p><strong>示例 1:</strong></p>

<pre><strong>输入:</strong> &quot;12&quot;
<strong>输出:</strong> 2
<strong>解释:</strong>&nbsp;它可以解码为 &quot;AB&quot;（1 2）或者 &quot;L&quot;（12）。
</pre>

<p><strong>示例&nbsp;2:</strong></p>

<pre><strong>输入:</strong> &quot;226&quot;
<strong>输出:</strong> 3
<strong>解释:</strong>&nbsp;它可以解码为 &quot;BZ&quot; (2 26), &quot;VF&quot; (22 6), 或者 &quot;BBF&quot; (2 2 6) 。
</pre>


## 解法：

对于字符串 s 的解码方式，可以是在 `s[0:-1]` 的基础上，将 `s[-1]` 解码，这样 s 的解码结果数就等于 `s[0:-1]` 的解码结果数。

也可以在 `s[0:-2]` 的基础上，将 `s[-2]` 和 `s[-1]` 合在一起解码，如果能够解码成功，其解码结果数就等于对 `s[0:-2]` 解码的结果数。

```python
class Solution:
    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """
        if len(s) == 0 or s[0] == '0':
            return 0
        
        if len(s) == 1:
            return 1
        
        a, b = 1, 1
        for i in range(2, len(s)):
            ans = 0
            if s[i] != '0':
                ans += b
            if s[i-1] == '1' or (s[i-1] == '2' and s[i] <= '6'):
                ans += a

            a = b
            b = ans

        return b
```