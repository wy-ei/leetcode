## 290. Word Pattern

- 难度： 简单
- 通过率： 34.3%
- 题目链接：[https://leetcode.com/problems/word-pattern](https://leetcode.com/problems/word-pattern)


## 题目描述

来源于 [https://leetcode-cn.com/](https://leetcode-cn.com/)

<p>给定一种 <code>pattern(模式)</code>&nbsp;和一个字符串&nbsp;<code>str</code>&nbsp;，判断 <code>str</code> 是否遵循相同的模式。</p>

<p>这里的<strong>遵循</strong>指完全匹配，例如，&nbsp;<code>pattern</code>&nbsp;里的每个字母和字符串&nbsp;<code>str</code><strong>&nbsp;</strong>中的每个非空单词之间存在着双向连接的对应模式。</p>

<p><strong>示例1:</strong></p>

<pre><strong>输入:</strong> pattern = <code>&quot;abba&quot;</code>, str = <code>&quot;dog cat cat dog&quot;</code>
<strong>输出:</strong> true</pre>

<p><strong>示例 2:</strong></p>

<pre><strong>输入:</strong>pattern = <code>&quot;abba&quot;</code>, str = <code>&quot;dog cat cat fish&quot;</code>
<strong>输出:</strong> false</pre>

<p><strong>示例 3:</strong></p>

<pre><strong>输入:</strong> pattern = <code>&quot;aaaa&quot;</code>, str = <code>&quot;dog cat cat dog&quot;</code>
<strong>输出:</strong> false</pre>

<p><strong>示例&nbsp;4:</strong></p>

<pre><strong>输入:</strong> pattern = <code>&quot;abba&quot;</code>, str = <code>&quot;dog dog dog dog&quot;</code>
<strong>输出:</strong> false</pre>

<p><strong>说明:</strong><br>
你可以假设&nbsp;<code>pattern</code>&nbsp;只包含小写字母，&nbsp;<code>str</code>&nbsp;包含了由单个空格分隔的小写字母。&nbsp; &nbsp;&nbsp;</p>


## 解法：