## 183. Customers Who Never Order

- 难度： 简单
- 通过率： 41.4%
- 题目链接：[https://leetcode.com/problems/customers-who-never-order](https://leetcode.com/problems/customers-who-never-order)


## 题目描述

来源于 [https://leetcode-cn.com/](https://leetcode-cn.com/)

<p>某网站包含两个表，<code>Customers</code> 表和 <code>Orders</code> 表。编写一个 SQL 查询，找出所有从不订购任何东西的客户。</p>

<p><code>Customers</code> 表：</p>

<pre>+----+-------+
| Id | Name  |
+----+-------+
| 1  | Joe   |
| 2  | Henry |
| 3  | Sam   |
| 4  | Max   |
+----+-------+
</pre>

<p><code>Orders</code> 表：</p>

<pre>+----+------------+
| Id | CustomerId |
+----+------------+
| 1  | 3          |
| 2  | 1          |
+----+------------+
</pre>

<p>例如给定上述表格，你的查询应返回：</p>

<pre>+-----------+
| Customers |
+-----------+
| Henry     |
| Max       |
+-----------+
</pre>


## 解法：