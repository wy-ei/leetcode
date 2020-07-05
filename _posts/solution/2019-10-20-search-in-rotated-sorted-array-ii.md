---
title: 搜索旋转排序数组 II
qid: 81
tags: [数组,二分查找]
---


- 难度： 中等
- 通过率： 32.5%
- 题目链接：[https://leetcode.com/problems/search-in-rotated-sorted-array-ii](https://leetcode.com/problems/search-in-rotated-sorted-array-ii)


## 题目描述

来源于 [https://leetcode-cn.com/](https://leetcode-cn.com/)

<p>假设按照升序排序的数组在预先未知的某个点上进行了旋转。</p>

<p>( 例如，数组&nbsp;<code>[0,0,1,2,2,5,6]</code>&nbsp;可能变为&nbsp;<code>[2,5,6,0,0,1,2]</code>&nbsp;)。</p>

<p>编写一个函数来判断给定的目标值是否存在于数组中。若存在返回&nbsp;<code>true</code>，否则返回&nbsp;<code>false</code>。</p>

<p><strong>示例&nbsp;1:</strong></p>

<pre><strong>输入:</strong> nums = [2<code>,5,6,0,0,1,2]</code>, target = 0
<strong>输出:</strong> true
</pre>

<p><strong>示例&nbsp;2:</strong></p>

<pre><strong>输入:</strong> nums = [2<code>,5,6,0,0,1,2]</code>, target = 3
<strong>输出:</strong> false</pre>

<p><strong>进阶:</strong></p>

<ul>
	<li>这是 <a href="https://leetcode-cn.com/problems/search-in-rotated-sorted-array/description/">搜索旋转排序数组</a>&nbsp;的延伸题目，本题中的&nbsp;<code>nums</code>&nbsp; 可能包含重复元素。</li>
	<li>这会影响到程序的时间复杂度吗？会有怎样的影响，为什么？</li>
</ul>


## 解法：

这个问题与 [Search in Rotated Sorted Array](./033-search-in-rotated-sorted-array.md) 的区别在于此问题中存在重复元素。

由此引发的问题是，旋转之后，数组后半部分不一定小于前半部分了。因此，在使用 `(nums[mid] >= nums[0]) == (target >= nums[0])` 判断 `nums[mid]` 和 `target` 是否位于同一部分时会出错。

原因在于旋转后的数组，头部和尾部元素的值可能相等。其实只需要去除数组尾部重复的元素，就能保证前半部分一定大于后半部分。

```
4 4 5 5 6 7 1 2 3 4 4 4 4
           ^

4 4 5 5 6 7 1 2 3
```

如此以来再使用 Search in Rotated Sorted Array 中的解法，就可以了。


```python
class Solution:
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: bool
        """
        
        lo = 0
        hi = len(nums) - 1
        inf = float('inf')

        if len(nums) == 0:
            return False

        while hi > lo and nums[lo] == nums[hi]:
            hi -= 1

        while lo <= hi:
            mid = lo + (hi-lo) // 2

            if (nums[mid] >= nums[0]) == (target >= nums[0]):
                num = nums[mid]
            else:
                if target < nums[0]:
                    num = -inf
                else:
                    num = inf

            if num == target:
                return True
            elif num < target:
                lo = mid + 1
            else:
                hi = mid - 1


        return False
```