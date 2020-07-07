---
title: 分割回文串
qid: 131
tags: [回溯算法]
---


- 难度： 中等
- 通过率： 38.7%
- 题目链接：[https://leetcode-cn.com/problems/palindrome-partitioning](https://leetcode-cn.com/problems/palindrome-partitioning)


## 题目描述

来源于 [https://leetcode-cn.com/](https://leetcode-cn.com/)

<p>给定一个字符串 <em>s</em>，将<em> s </em>分割成一些子串，使每个子串都是回文串。</p>

<p>返回 <em>s</em> 所有可能的分割方案。</p>

<p><strong>示例:</strong></p>

<pre><strong>输入:</strong>&nbsp;&quot;aab&quot;
<strong>输出:</strong>
[
  [&quot;aa&quot;,&quot;b&quot;],
  [&quot;a&quot;,&quot;a&quot;,&quot;b&quot;]
]</pre>


## 解法：

直接采用回溯法暴力搜索即可。

```python
class Solution:
    def partition(self, s: str) -> List[List[str]]:
        result = []
        
        def helper(s, res):
            if not s:
                result.append(res)
                return
                
            for i in range(len(s)):
                if s[:i+1] == s[:i+1][::-1]:
                    helper(s[i+1:], res + [s[:i+1]])
        
        helper(s, [])
        
        return result
```