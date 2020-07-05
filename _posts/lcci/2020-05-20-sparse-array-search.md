---
title: 稀疏数组搜索
qid: 10.05
tags: [二分查找]
---


- 难度：Easy
- 题目链接：[https://leetcode-cn.com/problems/sparse-array-search-lcci/](https://leetcode-cn.com/problems/sparse-array-search-lcci/)


## 题目描述

来源于 [https://leetcode-cn.com/](https://leetcode-cn.com/)

<p>稀疏数组搜索。有个排好序的字符串数组，其中散布着一些空字符串，编写一种方法，找出给定字符串的位置。</p>

<p><strong>示例1:</strong></p>

<pre><strong> 输入</strong>: words = [&quot;at&quot;, &quot;&quot;, &quot;&quot;, &quot;&quot;, &quot;ball&quot;, &quot;&quot;, &quot;&quot;, &quot;car&quot;, &quot;&quot;, &quot;&quot;,&quot;dad&quot;, &quot;&quot;, &quot;&quot;], s = &quot;ta&quot;
<strong> 输出</strong>：-1
<strong> 说明</strong>: 不存在返回-1。
</pre>

<p><strong>示例2:</strong></p>

<pre><strong> 输入</strong>：words = [&quot;at&quot;, &quot;&quot;, &quot;&quot;, &quot;&quot;, &quot;ball&quot;, &quot;&quot;, &quot;&quot;, &quot;car&quot;, &quot;&quot;, &quot;&quot;,&quot;dad&quot;, &quot;&quot;, &quot;&quot;], s = &quot;ball&quot;
<strong> 输出</strong>：4
</pre>

<p><strong>提示:</strong></p>

<ol>
	<li>words的长度在[1, 1000000]之间</li>
</ol>


## 解法：