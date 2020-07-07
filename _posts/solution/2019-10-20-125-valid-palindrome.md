---
title: 验证回文串
qid: 125
tags: [双指针,字符串]
---


- 难度： 简单
- 通过率： 29.5%
- 题目链接：[https://leetcode-cn.com/problems/valid-palindrome](https://leetcode-cn.com/problems/valid-palindrome)


## 题目描述

来源于 [https://leetcode-cn.com/](https://leetcode-cn.com/)

<p>给定一个字符串，验证它是否是回文串，只考虑字母和数字字符，可以忽略字母的大小写。</p>

<p><strong>说明：</strong>本题中，我们将空字符串定义为有效的回文串。</p>

<p><strong>示例 1:</strong></p>

<pre><strong>输入:</strong> &quot;A man, a plan, a canal: Panama&quot;
<strong>输出:</strong> true
</pre>

<p><strong>示例 2:</strong></p>

<pre><strong>输入:</strong> &quot;race a car&quot;
<strong>输出:</strong> false
</pre>


## 解法：

在 Python 中 `str.isalpha` 并不是只对 `a-zA-Z0-9` 返回真，而是对所有语言中的 “字母”， 即语言的基本组成，比如 `str.isalpha("你") -> True`。此处应该如果要限定英文字母和数字，需要使用 `str.isascii` 和 `str.isdigit` 但是 `str.isascii` 是 Python 3.7 新加的，leetcode 目前的 Python 环境还低于 Python 3.7。


```python
class Solution:
    def isPalindrome(self, s: str) -> bool:
        # s = [c for c in s if c.isascii() or c.isdigit()]
        s = [c for c in s if c.isalnum()]
        lo, hi = 0, len(s) - 1
        
        while lo < hi:
            if s[lo].lower() == s[hi].lower():
                lo += 1
                hi -= 1
            else:
                return False

        return True
```