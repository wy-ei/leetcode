## 230. Kth Smallest Element in a BST

- 难度： 中等
- 通过率： 48.9%
- 题目链接：[https://leetcode.com/problems/kth-smallest-element-in-a-bst](https://leetcode.com/problems/kth-smallest-element-in-a-bst)


### 题目描述

来源于 [https://leetcode-cn.com/](https://leetcode-cn.com/)

<p>给定一个二叉搜索树，编写一个函数&nbsp;<code>kthSmallest</code>&nbsp;来查找其中第&nbsp;<strong>k&nbsp;</strong>个最小的元素。</p>

<p><strong>说明：</strong><br>
你可以假设 k 总是有效的，1 &le; k &le; 二叉搜索树元素个数。</p>

<p><strong>示例 1:</strong></p>

<pre><strong>输入:</strong> root = [3,1,4,null,2], k = 1
   3
  / \
 1   4
  \
&nbsp;  2
<strong>输出:</strong> 1</pre>

<p><strong>示例 2:</strong></p>

<pre><strong>输入:</strong> root = [5,3,6,2,4,null,null,1], k = 3
       5
      / \
     3   6
    / \
   2   4
  /
 1
<strong>输出:</strong> 3</pre>

<p><strong>进阶：</strong><br>
如果二叉搜索树经常被修改（插入/删除操作）并且你需要频繁地查找第 k 小的值，你将如何优化&nbsp;<code>kthSmallest</code>&nbsp;函数？</p>


### 解法：