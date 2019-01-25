## 20. Valid Parentheses

- 难度： 简单
- 通过率： 35.4%
- 题目链接：[https://leetcode.com/problems/valid-parentheses](https://leetcode.com/problems/valid-parentheses)


## 题目描述

来源于 [https://leetcode-cn.com/](https://leetcode-cn.com/)

<p>给定一个只包括 <code>&#39;(&#39;</code>，<code>&#39;)&#39;</code>，<code>&#39;{&#39;</code>，<code>&#39;}&#39;</code>，<code>&#39;[&#39;</code>，<code>&#39;]&#39;</code>&nbsp;的字符串，判断字符串是否有效。</p>

<p>有效字符串需满足：</p>

<ol>
	<li>左括号必须用相同类型的右括号闭合。</li>
	<li>左括号必须以正确的顺序闭合。</li>
</ol>

<p>注意空字符串可被认为是有效字符串。</p>

<p><strong>示例 1:</strong></p>

<pre><strong>输入:</strong> &quot;()&quot;
<strong>输出:</strong> true
</pre>

<p><strong>示例&nbsp;2:</strong></p>

<pre><strong>输入:</strong> &quot;()[]{}&quot;
<strong>输出:</strong> true
</pre>

<p><strong>示例&nbsp;3:</strong></p>

<pre><strong>输入:</strong> &quot;(]&quot;
<strong>输出:</strong> false
</pre>

<p><strong>示例&nbsp;4:</strong></p>

<pre><strong>输入:</strong> &quot;([)]&quot;
<strong>输出:</strong> false
</pre>

<p><strong>示例&nbsp;5:</strong></p>

<pre><strong>输入:</strong> &quot;{[]}&quot;
<strong>输出:</strong> true</pre>


## 解法：

使用栈很容易解决，需要注意的是在 `pop` 的时候需要检查栈是否为空。

```python
class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        start = {'(', '[', '{'}
        mapping = {')': '(', ']': '[', '}': '{'}
        stack = []
        for c in s:
            if c in start:
                stack.append(c)
            elif len(stack) == 0 or stack.pop() != mapping[c]:
                return False
        return len(stack) == 0
```