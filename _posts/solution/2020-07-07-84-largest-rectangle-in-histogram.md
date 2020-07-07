---
title: 柱状图中最大的矩形
qid: 84
tag: [单调栈, 数组]
---

- 难度： 困难
- 通过率： 29.6%
- 题目链接：[https://leetcode-cn.com/problems/largest-rectangle-in-histogram](https://leetcode-cn.com/problems/largest-rectangle-in-histogram)


## 题目描述

来源于 [https://leetcode-cn.com/](https://leetcode-cn.com/)

<p>给定 <em>n</em> 个非负整数，用来表示柱状图中各个柱子的高度。每个柱子彼此相邻，且宽度为 1 。</p>

<p>求在该柱状图中，能够勾勒出来的矩形的最大面积。</p>

<p>&nbsp;</p>

<p><img src="https://assets.leetcode-cn.com/aliyun-lc-upload/uploads/2018/10/12/histogram.png"></p>

<p><small>以上是柱状图的示例，其中每个柱子的宽度为 1，给定的高度为&nbsp;<code>[2,1,5,6,2,3]</code>。</small></p>

<p>&nbsp;</p>

<p><img src="https://assets.leetcode-cn.com/aliyun-lc-upload/uploads/2018/10/12/histogram_area.png"></p>

<p><small>图中阴影部分为所能勾勒出的最大矩形面积，其面积为&nbsp;<code>10</code>&nbsp;个单位。</small></p>

<p>&nbsp;</p>

<p><strong>示例:</strong></p>

<pre><strong>输入:</strong> [2,1,5,6,2,3]
<strong>输出:</strong> 10</pre>


## 分析

对于每根柱子，尝试以该柱子的高度作为构成的矩阵的高，向两边扩张，直到遇到比当前柱子矮的。如此，就得到了宽度，进而得到面积。这种方法是时间复杂度为 `$O(n^2)$`。

如果柱子的按高度递增的顺序排列，对于每个柱子，以它作为矩形高度，矩形的宽度就是右边的柱子数量。因为右边的目标，肯定比该柱子要高。基于此想法，维护一个单调递增栈，在遇到一个比栈顶木板短的木板时，栈中的所有柱子就是递增排列的。只是这些柱子不一定是挨在一起的。因此需
基于下标得出矩形的宽度。

## 解法：单调栈


```cpp
class Solution {
  public:
    int largestRectangleArea(vector<int> &heights) {
        stack<int> stk;
        int area = 0;
        stk.push(-1);
        for (int i = 0; i <= heights.size(); i++) {
            int curr = i < heights.size() ? heights[i] : 0;
            while (stk.top() != -1 && curr < heights[stk.top()]) {
                int height = heights[stk.top()];
                stk.pop();

                int width = i - stk.top() - 1;
                area = max(area, height * width);
            }
            stk.push(i);
        }
        return area;
    }
};
```