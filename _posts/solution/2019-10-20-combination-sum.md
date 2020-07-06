---
title: 组合总和
qid: 39
tags: [数组,回溯算法]
---


- 难度： 中等
- 通过率： 45.4%
- 题目链接：[https://leetcode-cn.com/problems/combination-sum](https://leetcode-cn.com/problems/combination-sum)


## 题目描述

来源于 [https://leetcode-cn.com/](https://leetcode-cn.com/)

<p>给定一个<strong>无重复元素</strong>的数组&nbsp;<code>candidates</code>&nbsp;和一个目标数&nbsp;<code>target</code>&nbsp;，找出&nbsp;<code>candidates</code>&nbsp;中所有可以使数字和为&nbsp;<code>target</code>&nbsp;的组合。</p>

<p><code>candidates</code>&nbsp;中的数字可以无限制重复被选取。</p>

<p><strong>说明：</strong></p>

<ul>
	<li>所有数字（包括&nbsp;<code>target</code>）都是正整数。</li>
	<li>解集不能包含重复的组合。&nbsp;</li>
</ul>

<p><strong>示例&nbsp;1:</strong></p>

<pre><strong>输入:</strong> candidates = <code>[2,3,6,7], </code>target = <code>7</code>,
<strong>所求解集为:</strong>
[
  [7],
  [2,2,3]
]
</pre>

<p><strong>示例&nbsp;2:</strong></p>

<pre><strong>输入:</strong> candidates = [2,3,5]<code>, </code>target = 8,
<strong>所求解集为:</strong>
[
&nbsp; [2,2,2,2],
&nbsp; [2,3,3],
&nbsp; [3,5]
]</pre>


## 解法：

此问题可以采用回溯法来搜索可行解。

回溯算法是一种搜索问题解的方法，基本思想是，对解空间树进行深度优先遍历，在遍历过程中，根据当前状态决定是否继续前进。回溯算法解决问题的一般步骤为：

1. 根据实际问题定义解空间，解空间中包含问题的解
2. 采用深度优先搜索对解空间进行搜索
3. 在搜索过程中用根据某种条件避免不必要的搜索，即对解空间树进行剪枝。

本题，本题的解空间就是 `candidates` 数组中所有元素的各种可能的组合，其中每个元素都可以重复任意次。

将解空间看成一个树，其中第一层包含 `candidates` 中所有元素，其中每个元素对应一个节点，第二层中 1 对应的节点为 `{1,2,3,4,5}`, 2 对应的节点为 `{2,3,4,5}` …… 第三层中各个节点的子节点依然这样对应。

```
1 层                  [1,2,3,4,5]

2 层     [1,2,3,4,5] [2,3,4,5]  [3,4,5] [4,5] [5]
        
3 层  [1,2,3,4,5] [2,3,4,5] [3,4,5] [4,5] [5]  ...
```

在进行深度优先搜索的过程中，需要保存当前已经遍历过的节点，因此在递归调用的时候需要使用一个数组保存这些数。如果当前节点的值等于 target，那么就得到了问题的一个解。如果当前值大于 target，那么深入下一层后，所搜寻的 target 就要减去当前节点的值。

使用文字描述算法思想真不是一件容易的事情，佩服写算法书的人。我想还是直接看代码来的清楚：

```python
class Solution:
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        # 保存遍历过程中遇到的可行解
        results = []
        
        self._combinationSum(candidates, 0, [], target, results)
        
        return results
        
    
    # 这里的参数 i 用于记录当前遍历的值是数组中的第几个元素，
    # 因为在下一层遍历过程中，不在需要考虑此下标之前的那些元素。
    def _combinationSum(self, candidates, i, nums, target, results):
        for j in range(i, len(candidates)):
            n = candidates[j]
            if n == target:
                results.append(nums + [n])
            elif n < target:
                self._combinationSum(candidates, j, nums + [n], target - n, results)
```