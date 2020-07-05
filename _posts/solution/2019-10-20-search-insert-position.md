---
title: 搜索插入位置
qid: 35
tags: [数组,二分查找]
---


- 难度： 简单
- 通过率： 40.2%
- 题目链接：[https://leetcode.com/problems/search-insert-position](https://leetcode.com/problems/search-insert-position)


## 题目描述

来源于 [https://leetcode-cn.com/](https://leetcode-cn.com/)

<p>给定一个排序数组和一个目标值，在数组中找到目标值，并返回其索引。如果目标值不存在于数组中，返回它将会被按顺序插入的位置。</p>

<p>你可以假设数组中无重复元素。</p>

<p><strong>示例 1:</strong></p>

<pre><strong>输入:</strong> [1,3,5,6], 5
<strong>输出:</strong> 2
</pre>

<p><strong>示例&nbsp;2:</strong></p>

<pre><strong>输入:</strong> [1,3,5,6], 2
<strong>输出:</strong> 1
</pre>

<p><strong>示例 3:</strong></p>

<pre><strong>输入:</strong> [1,3,5,6], 7
<strong>输出:</strong> 4
</pre>

<p><strong>示例 4:</strong></p>

<pre><strong>输入:</strong> [1,3,5,6], 0
<strong>输出:</strong> 0
</pre>


## 解法：

二分查找而已，二分查找结束后，如果没有找到 `lo` 会指向在有序数组中 target 该插入的位置（如果要将 target 插入数组的话）。 

```python
def searchInsert(nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: int
    """

    lo = 0
    hi = len(nums)

    while lo < hi:
        mid = lo + (hi - lo) // 2

        if nums[mid] < target:
            lo = mid + 1
        elif nums[mid] > target:
            hi = mid
        else:
            return mid

    return lo
```