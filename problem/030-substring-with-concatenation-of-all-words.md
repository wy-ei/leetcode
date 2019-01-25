## 30. Substring with Concatenation of All Words

- 难度： 困难
- 通过率： 22.7%
- 题目链接：[https://leetcode.com/problems/substring-with-concatenation-of-all-words](https://leetcode.com/problems/substring-with-concatenation-of-all-words)


## 题目描述

来源于 [https://leetcode-cn.com/](https://leetcode-cn.com/)

<p>给定一个字符串&nbsp;<strong>s&nbsp;</strong>和一些长度相同的单词&nbsp;<strong>words。</strong>在<strong> s </strong>中找出可以恰好串联&nbsp;<strong>words&nbsp;</strong>中所有单词的子串的起始位置。</p>

<p>注意子串要与&nbsp;<strong>words </strong>中的单词完全匹配，中间不能有其他字符，但不需要考虑&nbsp;<strong>words&nbsp;</strong>中单词串联的顺序。</p>

<p><strong>示例 1:</strong></p>

<pre><strong>输入:
  s =</strong> &quot;barfoothefoobarman&quot;,
<strong>  words = </strong>[&quot;foo&quot;,&quot;bar&quot;]
<strong>输出:</strong> <code>[0,9]</code>
<strong>解释:</strong> 从索引 0 和 9 开始的子串分别是 &quot;barfoor&quot; 和 &quot;foobar&quot; 。
输出的顺序不重要, [9,0] 也是有效答案。
</pre>

<p><strong>示例 2:</strong></p>

<pre><strong>输入:
  s =</strong> &quot;wordgoodstudentgoodword&quot;,
<strong>  words = </strong>[&quot;word&quot;,&quot;student&quot;]
<strong>输出:</strong> <code>[]</code>
</pre>


## 解法：