## 108. Convert Sorted Array to Binary Search Tree

- 难度： 简单
- 通过率： 48.2%
- 题目链接：[https://leetcode.com/problems/convert-sorted-array-to-binary-search-tree](https://leetcode.com/problems/convert-sorted-array-to-binary-search-tree)


### 题目描述

来源于 [https://leetcode-cn.com/](https://leetcode-cn.com/)

<p>将一个按照升序排列的有序数组，转换为一棵高度平衡二叉搜索树。</p>

<p>本题中，一个高度平衡二叉树是指一个二叉树<em>每个节点&nbsp;</em>的左右两个子树的高度差的绝对值不超过 1。</p>

<p><strong>示例:</strong></p>

<pre>给定有序数组: [-10,-3,0,5,9],

一个可能的答案是：[0,-3,9,-10,null,5]，它可以表示下面这个高度平衡二叉搜索树：

      0
     / \
   -3   9
   /   /
 -10  5
</pre>


### 解法：