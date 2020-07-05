---
title: 特定深度节点链表
qid: 04.03
tags: [树,广度优先搜索]
---


- 难度：Medium
- 题目链接：[https://leetcode-cn.com/problems/list-of-depth-lcci/](https://leetcode-cn.com/problems/list-of-depth-lcci/)


## 题目描述

来源于 [https://leetcode-cn.com/](https://leetcode-cn.com/)

<p>给定一棵二叉树，设计一个算法，创建含有某一深度上所有节点的链表（比如，若一棵树的深度为 <code>D</code>，则会创建出 <code>D</code> 个链表）。返回一个包含所有深度的链表的数组。</p>

<p>&nbsp;</p>

<p><strong>示例：</strong></p>

<pre><strong>输入：</strong>[1,2,3,4,5,null,7,8]

        1
       /  \ 
      2    3
     / \    \ 
    4   5    7
   /
  8

<strong>输出：</strong>[[1],[2,3],[4,5,7],[8]]
</pre>


## 解法：

层次遍历，在每一层，建立链表即可，不再写了。
