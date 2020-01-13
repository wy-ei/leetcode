## 165. Compare Version Numbers

- 难度： 中等
- 通过率： 22.1%
- 题目链接：[https://leetcode.com/problems/compare-version-numbers](https://leetcode.com/problems/compare-version-numbers)


## 题目描述

来源于 [https://leetcode-cn.com/](https://leetcode-cn.com/)

<p>比较两个版本号 <em>version1&nbsp;</em>和 <em>version2</em>。<br>
如果&nbsp;<code><em>version1&nbsp;</em>&gt;&nbsp;<em>version2</em></code>&nbsp;返回&nbsp;<code>1</code>，如果&nbsp;<code><em>version1&nbsp;</em>&lt;&nbsp;<em>version2</em></code> 返回 <code>-1</code>， 除此之外返回 <code>0</code>。</p>

<p>你可以假设版本字符串非空，并且只包含数字和&nbsp;<code>.</code> 字符。</p>

<p>&nbsp;<code>.</code> 字符不代表小数点，而是用于分隔数字序列。</p>

<p>例如，<code>2.5</code> 不是&ldquo;两个半&rdquo;，也不是&ldquo;差一半到三&rdquo;，而是第二版中的第五个小版本。</p>

<p><strong>示例&nbsp;1:</strong></p>

<pre><strong>输入:</strong> <code><em>version1</em></code> = &quot;0.1&quot;, <code><em>version2</em></code> = &quot;1.1&quot;
<strong>输出:</strong> -1</pre>

<p><strong>示例 2:</strong></p>

<pre><strong>输入: </strong><code><em>version1</em></code> = &quot;1.0.1&quot;, <code><em>version2</em></code> = &quot;1&quot;
<strong>输出:</strong> 1</pre>

<p><strong>示例 3:</strong></p>

<pre><strong>输入:</strong> <code><em>version1</em></code> = &quot;7.5.2.4&quot;, <code><em>version2</em></code> = &quot;7.5.3&quot;
<strong>输出:</strong> -1</pre>


## 解法：