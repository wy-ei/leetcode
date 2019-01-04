## 149. Max Points on a Line

- 难度： 困难
- 通过率： 15.4%
- 题目链接：[https://leetcode.com/problems/max-points-on-a-line](https://leetcode.com/problems/max-points-on-a-line)


### 题目描述

来源于 [https://leetcode-cn.com/](https://leetcode-cn.com/)

<p>给定一个二维平面，平面上有&nbsp;<em>n&nbsp;</em>个点，求最多有多少个点在同一条直线上。</p>

<p><strong>示例 1:</strong></p>

<pre><strong>输入:</strong> [[1,1],[2,2],[3,3]]
<strong>输出:</strong> 3
<strong>解释:</strong>
^
|
| &nbsp; &nbsp; &nbsp; &nbsp;o
| &nbsp; &nbsp; o
| &nbsp;o &nbsp;
+-------------&gt;
0 &nbsp;1 &nbsp;2 &nbsp;3  4
</pre>

<p><strong>示例&nbsp;2:</strong></p>

<pre><strong>输入:</strong> [[1,1],[3,2],[5,3],[4,1],[2,3],[1,4]]
<strong>输出:</strong> 4
<strong>解释:</strong>
^
|
|  o
| &nbsp;&nbsp;&nbsp;&nbsp;o&nbsp;&nbsp;      o
| &nbsp;&nbsp;&nbsp;&nbsp;   o
| &nbsp;o &nbsp;      o
+-------------------&gt;
0 &nbsp;1 &nbsp;2 &nbsp;3 &nbsp;4 &nbsp;5 &nbsp;6</pre>


### 解法：