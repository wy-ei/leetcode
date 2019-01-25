## 181. Employees Earning More Than Their Managers

- 难度： 简单
- 通过率： 43.6%
- 题目链接：[https://leetcode.com/problems/employees-earning-more-than-their-managers](https://leetcode.com/problems/employees-earning-more-than-their-managers)


## 题目描述

来源于 [https://leetcode-cn.com/](https://leetcode-cn.com/)

<p><code>Employee</code>&nbsp;表包含所有员工，他们的经理也属于员工。每个员工都有一个 Id，此外还有一列对应员工的经理的 Id。</p>

<pre>+----+-------+--------+-----------+
| Id | Name  | Salary | ManagerId |
+----+-------+--------+-----------+
| 1  | Joe   | 70000  | 3         |
| 2  | Henry | 80000  | 4         |
| 3  | Sam   | 60000  | NULL      |
| 4  | Max   | 90000  | NULL      |
+----+-------+--------+-----------+
</pre>

<p>给定&nbsp;<code>Employee</code>&nbsp;表，编写一个 SQL 查询，该查询可以获取收入超过他们经理的员工的姓名。在上面的表格中，Joe 是唯一一个收入超过他的经理的员工。</p>

<pre>+----------+
| Employee |
+----------+
| Joe      |
+----------+
</pre>


## 解法：