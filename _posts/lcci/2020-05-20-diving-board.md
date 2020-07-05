---
title: 跳水板
qid: 16.11
tags: [递归,记忆化]
---


- 难度：Easy
- 题目链接：[https://leetcode-cn.com/problems/diving-board-lcci/](https://leetcode-cn.com/problems/diving-board-lcci/)


## 题目描述

来源于 [https://leetcode-cn.com/](https://leetcode-cn.com/)

<p>你正在使用一堆木板建造跳水板。有两种类型的木板，其中长度较短的木板长度为<code>shorter</code>，长度较长的木板长度为<code>longer</code>。你必须正好使用<code>k</code>块木板。编写一个方法，生成跳水板所有可能的长度。</p>
<p>返回的长度需要从小到大排列。</p>
<p><strong>示例：</strong></p>
<pre><strong>输入：</strong>
shorter = 1
longer = 2
k = 3
<strong>输出：</strong> {3,4,5,6}
</pre>
<p><strong>提示：</strong></p>
<ul>
<li>0 < shorter <= longer</li>
<li>0 <= k <= 100000</li>
</ul>


## 解法：