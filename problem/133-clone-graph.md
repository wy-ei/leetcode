## 133. Clone Graph

- 难度： 中等
- 通过率： 25.1%
- 题目链接：[https://leetcode.com/problems/clone-graph](https://leetcode.com/problems/clone-graph)


### 题目描述

来源于 [https://leetcode-cn.com/](https://leetcode-cn.com/)

<p>克隆一张无向图，图中的每个节点包含一个&nbsp;<code>label</code>&nbsp;（标签）和一个&nbsp;<code>neighbors</code>&nbsp;（邻接点）列表 。</p>

<p><strong>OJ的无向图序列化：</strong></p>

<p>节点被唯一标记。</p>

<p>我们用 <code>#</code> 作为每个节点的分隔符，用&nbsp;<code>,</code>&nbsp;作为节点标签和邻接点的分隔符。</p>

<p>例如，序列化无向图 <code>{0,1,2#1,2#2,2}</code>。</p>

<p>该图总共有三个节点, 被两个分隔符&nbsp; <code>#</code>&nbsp;分为三部分。&nbsp;</p>

<ol>
	<li>第一个节点的标签为 <code>0</code>，存在从节点 <code>0</code> 到节点 <code>1</code> 和节点 <code>2</code> 的两条边。</li>
	<li>第二个节点的标签为 <code>1</code>，存在从节点 <code>1</code> 到节点 <code>2</code> 的一条边。</li>
	<li>第三个节点的标签为 <code>2</code>，存在从节点 <code>2</code> 到节点 <code>2</code> (本身) 的一条边，从而形成自环。</li>
</ol>

<p>我们将图形可视化如下：</p>

<pre>       1
      / \
     /   \
    0 --- 2
         / \
         \_/
</pre>


### 解法：