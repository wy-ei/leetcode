---
title: 旋转图像
qid: 48
tags: [数组]
---


- 难度： 中等
- 通过率： 45.6%
- 题目链接：[https://leetcode-cn.com/problems/rotate-image](https://leetcode-cn.com/problems/rotate-image)


## 题目描述

来源于 [https://leetcode-cn.com/](https://leetcode-cn.com/)

<p>给定一个 <em>n&nbsp;</em>&times;&nbsp;<em>n</em> 的二维矩阵表示一个图像。</p>

<p>将图像顺时针旋转 90 度。</p>

<p><strong>说明：</strong></p>

<p>你必须在<strong><a href="https://baike.baidu.com/item/%E5%8E%9F%E5%9C%B0%E7%AE%97%E6%B3%95" target="_blank">原地</a></strong>旋转图像，这意味着你需要直接修改输入的二维矩阵。<strong>请不要</strong>使用另一个矩阵来旋转图像。</p>

<p><strong>示例 1:</strong></p>

<pre>给定 <strong>matrix</strong> = 
[
  [1,2,3],
  [4,5,6],
  [7,8,9]
],

<strong>原地</strong>旋转输入矩阵，使其变为:
[
  [7,4,1],
  [8,5,2],
  [9,6,3]
]
</pre>

<p><strong>示例 2:</strong></p>

<pre>给定 <strong>matrix</strong> =
[
  [ 5, 1, 9,11],
  [ 2, 4, 8,10],
  [13, 3, 6, 7],
  [15,14,12,16]
], 

<strong>原地</strong>旋转输入矩阵，使其变为:
[
  [15,13, 2, 5],
  [14, 3, 4, 1],
  [12, 6, 8, 9],
  [16, 7,10,11]
]
</pre>


## 解法：

从外层向内，逐层旋转。

```c++
class Solution {
public:
    void rotate(vector<vector<int>>& matrix) {
        if(matrix.empty() || matrix.back().empty()){
            return;
        }
        int row_lo = 0, row_hi = matrix.size() - 1;
        int col_lo = 0, col_hi = matrix.back().size() - 1;
        while(row_lo < row_hi){
            for(int i=0; i < row_hi - row_lo; i++){
                int t = matrix[row_lo][col_lo + i];
                matrix[row_lo][col_lo + i] = matrix[row_hi-i][col_lo];
                matrix[row_hi-i][col_lo] = matrix[row_hi][col_hi-i];
                matrix[row_hi][col_hi-i] = matrix[row_lo + i][col_hi];
                matrix[row_lo + i][col_hi] = t;
            }
            row_lo++;
            row_hi--;
            col_lo++;
            col_hi--;
        }
    }
};
```