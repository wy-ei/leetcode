---
title: 组合
qid: 77
tags: [回溯算法]
---


- 难度： 中等
- 通过率： 45.0%
- 题目链接：[https://leetcode-cn.com/problems/combinations](https://leetcode-cn.com/problems/combinations)


## 题目描述

来源于 [https://leetcode-cn.com/](https://leetcode-cn.com/)

<p>给定两个整数 <em>n</em> 和 <em>k</em>，返回 1 ... <em>n </em>中所有可能的 <em>k</em> 个数的组合。</p>

<p><strong>示例:</strong></p>

<pre><strong>输入:</strong>&nbsp;n = 4, k = 2
<strong>输出:</strong>
[
  [2,4],
  [3,4],
  [2,3],
  [1,2],
  [1,3],
  [1,4],
]</pre>


## 解法：

遇到组合问题，我就只能想到深度优先去遍历解空间。

每一个分支下面的节点可取值的范围需要设置的恰当，避免无意义的搜索。比如第一层就不应该有 4，否则第二层就没得可选的数字了。每个分支下面的可选数字范围为`[父节点+1, n-k+depth]`。

```
k=2, n=4

  1      2    3    -- depth=1 
 /|\    / \   |
2 3 4  3   4  4    -- deoth=2
| | |  |   |  |
1 1 1  2   2  3   
2 3 4  3   4  4
```


 
```python
def combine(self, n, k):
    """
    :type n: int
    :type k: int
    :rtype: List[List[int]]
    """

    results = []

    def __combine(i, depth, comb):
        if depth == k + 1:
            results.append(comb)
            return
        for i in range(i, n - k + depth + 1):
            __combine(i + 1, depth + 1, comb + [i])

    __combine(1, 1, [])

    return results
```