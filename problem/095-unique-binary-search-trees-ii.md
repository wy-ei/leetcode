## 95. Unique Binary Search Trees II

- 难度： 中等
- 通过率： 34.2%
- 题目链接：[https://leetcode.com/problems/unique-binary-search-trees-ii](https://leetcode.com/problems/unique-binary-search-trees-ii)


## 题目描述

来源于 [https://leetcode-cn.com/](https://leetcode-cn.com/)

<p>给定一个整数 <em>n</em>，生成所有由 1 ...&nbsp;<em>n</em> 为节点所组成的<strong>二叉搜索树</strong>。</p>

<p><strong>示例:</strong></p>

<pre><strong>输入:</strong> 3
<strong>输出:</strong>
[
&nbsp; [1,null,3,2],
&nbsp; [3,2,null,1],
&nbsp; [3,1,null,null,2],
&nbsp; [2,1,3],
&nbsp; [1,null,2,null,3]
]
<strong>解释:</strong>
以上的输出对应以下 5 种不同结构的二叉搜索树：

   1         3     3      2      1
    \       /     /      / \      \
     3     2     1      1   3      2
    /     /       \                 \
   2     1         2                 3
</pre>


## 解法：