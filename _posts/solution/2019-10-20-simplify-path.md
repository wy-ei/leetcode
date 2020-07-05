---
title: 简化路径
qid: 71
tags: [栈,字符串]
---


- 难度： 中等
- 通过率： 27.7%
- 题目链接：[https://leetcode.com/problems/simplify-path](https://leetcode.com/problems/simplify-path)


## 题目描述

来源于 [https://leetcode-cn.com/](https://leetcode-cn.com/)

<p>给定一个文档 (Unix-style) 的完全路径，请进行路径简化。</p>

<p>例如，<br>
<strong>path</strong> = <code>&quot;/home/&quot;</code>, =&gt; <code>&quot;/home&quot;</code><br>
<strong>path</strong> = <code>&quot;/a/./b/../../c/&quot;</code>, =&gt; <code>&quot;/c&quot;</code></p>

<p><strong>边界情况:</strong></p>

<ul>
	<li>你是否考虑了 路径 =&nbsp;<code>&quot;/../&quot;</code>&nbsp;的情况？<br>
	在这种情况下，你需返回&nbsp;<code>&quot;/&quot;</code>&nbsp;。</li>
	<li>此外，路径中也可能包含多个斜杠&nbsp;<code>&#39;/&#39;</code>&nbsp;，如&nbsp;<code>&quot;/home//foo/&quot;</code>&nbsp;。<br>
	在这种情况下，你可忽略多余的斜杠，返回&nbsp;<code>&quot;/home/foo&quot;</code>&nbsp;。</li>
</ul>


## 解法：

```python
<<< path = '/a/b/./c//d/../e/f'
<<< path.split('/')
>>> ['', 'a', 'b', '.', 'c', '', 'd', '..', 'e', 'f']
```

遇到空白跳过，遇到 `.` 跳过，遇到字符将字符入栈，遇到 `..` 出栈一个字符。

```python
class Solution:
    def simplifyPath(self, path):
        spans = path.split('/')
        stack = []

        for span in spans:
            if span == '' or span == '.':
                continue
                
            if span == '..' and len(stack) > 0:
                stack.pop()
                continue
                
            stack.append(span)

        return '/' + '/'.join(stack)
 ```