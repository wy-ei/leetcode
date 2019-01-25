## 117. Populating Next Right Pointers in Each Node II

- 难度： 中等
- 通过率： 33.3%
- 题目链接：[https://leetcode.com/problems/populating-next-right-pointers-in-each-node-ii](https://leetcode.com/problems/populating-next-right-pointers-in-each-node-ii)


## 题目描述

来源于 [https://leetcode-cn.com/](https://leetcode-cn.com/)

<p>给定一个二叉树</p>

<pre>struct TreeLinkNode {
  TreeLinkNode *left;
  TreeLinkNode *right;
  TreeLinkNode *next;
}
</pre>

<p>填充它的每个 next 指针，让这个指针指向其下一个右侧节点。如果找不到下一个右侧节点，则将 next 指针设置为 <code>NULL</code>。</p>

<p>初始状态下，所有&nbsp;next 指针都被设置为 <code>NULL</code>。</p>

<p><strong>说明:</strong></p>

<ul>
	<li>你只能使用额外常数空间。</li>
	<li>使用递归解题也符合要求，本题中递归程序占用的栈空间不算做额外的空间复杂度。</li>
</ul>

<p><strong>示例:</strong></p>

<p>给定二叉树，</p>

<pre>     1
   /  \
  2    3
 / \    \
4   5    7
</pre>

<p>调用你的函数后，该二叉树变为：</p>

<pre>     1 -&gt; NULL
   /  \
  2 -&gt; 3 -&gt; NULL
 / \    \
4-&gt; 5 -&gt; 7 -&gt; NULL</pre>


## 解法：