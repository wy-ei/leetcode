## 185. Department Top Three Salaries

- 难度： 困难
- 通过率： 22.7%
- 题目链接：[https://leetcode.com/problems/department-top-three-salaries](https://leetcode.com/problems/department-top-three-salaries)


## 题目描述

来源于 [https://leetcode-cn.com/](https://leetcode-cn.com/)

<p><code>Employee</code> 表包含所有员工信息，每个员工有其对应的&nbsp;Id, salary 和 department Id 。</p>

<pre>+----+-------+--------+--------------+
| Id | Name  | Salary | DepartmentId |
+----+-------+--------+--------------+
| 1  | Joe   | 70000  | 1            |
| 2  | Henry | 80000  | 2            |
| 3  | Sam   | 60000  | 2            |
| 4  | Max   | 90000  | 1            |
| 5  | Janet | 69000  | 1            |
| 6  | Randy | 85000  | 1            |
+----+-------+--------+--------------+
</pre>

<p><code>Department</code> 表包含公司所有部门的信息。</p>

<pre>+----+----------+
| Id | Name     |
+----+----------+
| 1  | IT       |
| 2  | Sales    |
+----+----------+
</pre>

<p>编写一个&nbsp;SQL 查询，找出每个部门工资前三高的员工。例如，根据上述给定的表格，查询结果应返回：</p>

<pre>+------------+----------+--------+
| Department | Employee | Salary |
+------------+----------+--------+
| IT         | Max      | 90000  |
| IT         | Randy    | 85000  |
| IT         | Joe      | 70000  |
| Sales      | Henry    | 80000  |
| Sales      | Sam      | 60000  |
+------------+----------+--------+
</pre>


## 解法：