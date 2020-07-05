---
title: 合并区间
qid: 56
tags: [排序,数组]
---


- 难度： 中等
- 通过率： 34.1%
- 题目链接：[https://leetcode.com/problems/merge-intervals](https://leetcode.com/problems/merge-intervals)


## 题目描述

来源于 [https://leetcode-cn.com/](https://leetcode-cn.com/)

<p>给出一个区间的集合，请合并所有重叠的区间。</p>

<p><strong>示例 1:</strong></p>

<pre><strong>输入:</strong> [[1,3],[2,6],[8,10],[15,18]]
<strong>输出:</strong> [[1,6],[8,10],[15,18]]
<strong>解释:</strong> 区间 [1,3] 和 [2,6] 重叠, 将它们合并为 [1,6].
</pre>

<p><strong>示例&nbsp;2:</strong></p>

<pre><strong>输入:</strong> [[1,4],[4,5]]
<strong>输出:</strong> [[1,5]]
<strong>解释:</strong> 区间 [1,4] 和 [4,5] 可被视为重叠区间。</pre>


## 解法：

先按照 `interval.start` 排序

```
---  <-- i
  ------
   ----
           ----
             ---
```

遍历所有 `interval`，只要有重合，就把它们合并到第一个上面去。

```
--------  <-- i
  ------
   ----
           ----
             ---
```

在合并过程中，使用 i 指向重合区间的第一个 interval，遇到不重合的，把该 interval 移动到 i+1 处。

```
--------
           ----  <-- i
  ----
           ----  <-- 拷贝此到 i 处
             --- <-- 合并到  interval[i] 上
```

最终结果为 `intervals[0:i+1]`


```python
class Solution:
    def merge(self, intervals):
        intervals.sort(key=lambda interval: interval[0])
        
        i = 0
        for interval in intervals:
            if interval[0] <= intervals[i][1]:
                intervals[i][1] = max(intervals[i][1], interval[1])
            else:
                i += 1
                intervals[i] = interval
        
        return intervals[0:i+1]
```