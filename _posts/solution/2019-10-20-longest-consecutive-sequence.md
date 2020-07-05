---
title: 最长连续序列
qid: 128
tags: [并查集,数组]
---


- 难度： 困难
- 通过率： 40.3%
- 题目链接：[https://leetcode.com/problems/longest-consecutive-sequence](https://leetcode.com/problems/longest-consecutive-sequence)


## 题目描述

来源于 [https://leetcode-cn.com/](https://leetcode-cn.com/)

<p>给定一个未排序的整数数组，找出最长连续序列的长度。</p>

<p>要求算法的时间复杂度为&nbsp;<em>O(n)</em>。</p>

<p><strong>示例:</strong></p>

<pre><strong>输入:</strong>&nbsp;[100, 4, 200, 1, 3, 2]
<strong>输出:</strong> 4
<strong>解释:</strong> 最长连续序列是 <code>[1, 2, 3, 4]。它的长度为 4。</code></pre>


## 解法：

用一个 map 记录各个数字所在序列的最大长度。对任意数字，有以下几种情况：

1. 该数是序列的端点
2. 该数连接两个序列

对于 `num` 而言，如果 map 中已经有了 `num` 则不做任何处理。

如果 `num-1` 出现在 map 中，则说明 `num` 是右端点。如果 `num+1` 出现在 map 中，说明 `num` 是左端点。整个序列的长度为左右两边的子序列加 1。

为了记录更新后的新序列长度，只需要更新左右端点对应的序列长度即可。`num-left` 就是左端点，`num+left` 就是右端点。在 map 中更新这两个键的值为新序列的长度即可。


```python
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        mp = {}
        max_len = 0
        
        for num in nums:
            if num in mp:
                continue
                
            left = mp.get(num-1, 0)
            right = mp.get(num+1, 0)
            
            total = left + right + 1
            
            mp[num] = total
            mp[num - left] = total
            mp[num + right] = total
        
            max_len = max(max_len, total)
            
        return max_len
```