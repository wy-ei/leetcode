---
title: 零矩阵
qid: 01.08
tags: [数组]
---


- 难度：Medium
- 题目链接：[https://leetcode-cn.com/problems/zero-matrix-lcci/](https://leetcode-cn.com/problems/zero-matrix-lcci/)


## 题目描述

来源于 [https://leetcode-cn.com/](https://leetcode-cn.com/)

<p>编写一种算法，若M × N矩阵中某个元素为0，则将其所在的行与列清零。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre><strong>输入：</strong>
[
  [1,1,1],
  [1,0,1],
  [1,1,1]
]
<strong>输出：</strong>
[
  [1,0,1],
  [0,0,0],
  [1,0,1]
]
</pre>

<p><strong>示例 2：</strong></p>

<pre><strong>输入：</strong>
[
  [0,1,2,0],
  [3,4,5,2],
  [1,3,1,5]
]
<strong>输出：</strong>
[
  [0,0,0,0],
  [0,4,5,0],
  [0,3,1,0]
]
</pre>


## 解法：

遍历矩阵，收集需要清空的行与列，然后将对应的行和列清空。这需要额外的存储空间，但是相当容易理解。

```c++
class Solution {
public:
    void setZeroes(vector<vector<int>>& matrix) {
        if(matrix.empty() || matrix.front().empty()){
            return;
        }

        int n_rows = matrix.size();
        int n_cols = matrix[0].size();
        unordered_set<int> rows, cols;
        
        for(int row=0;row<n_rows;row++){
            for(int col=0;col<n_cols;col++){
                if(matrix[row][col] == 0){
                    rows.insert(row);
                    cols.insert(col);
                }
            }
        }

        for(auto row: rows){
            clear_row(matrix, row);
        }

        for(auto col: cols){
            clear_col(matrix, col);
        }
    }
private:
    static void clear_row(vector<vector<int>>& matrix, int row) {
        fill(matrix[row].begin(), matrix[row].end(), 0);
    }

    static void clear_col(vector<vector<int>>& matrix, int col) {
        for(auto & row : matrix){
            row[col] = 0;
        }
    }
};
```

还有一种思路可以不使用额外的空间，使用第一行记录各列中是否有 0，使用第一列来记录各行是否有 0。由于第一行和第一列会被修改，因此可以率先统计第一行和第一列是否有零。

```c++
class Solution {
public:
    void setZeroes(vector<vector<int>>& matrix) {
        if(matrix.empty() || matrix.front().empty()){
            return;
        }

        int n_rows = matrix.size();
        int n_cols = matrix[0].size();
        
        bool first_row_has_zero = false;
        bool first_col_has_zero = false;

        
        for(int col=0;col<n_cols;col++){
            if(matrix[0][col] == 0){
                first_row_has_zero = true;
                break;
            }
        }
        for(int row=0;row<n_rows;row++){
            if(matrix[row][0] == 0){
                first_col_has_zero = true;
                break;
            }
        }

        for(int row=1;row<n_rows;row++){
            for(int col=1;col<n_cols;col++){
                if(matrix[row][col] == 0){
                    matrix[0][col] = 0;
                    matrix[row][0] = 0;
                }
            }
        }

        for(int col=1;col<n_cols;col++){
            if(matrix[0][col] == 0){
                clear_col(matrix, col);
            }
        }

        for(int row=1;row<n_rows;row++){
            if(matrix[row][0] == 0){
                clear_row(matrix, row);
            }
        }

        if(first_row_has_zero){
            clear_row(matrix, 0);
        }

        if(first_col_has_zero){
            clear_col(matrix, 0);
        }
    }
private:
    static void clear_row(vector<vector<int>>& matrix, int row) {
        fill(matrix[row].begin(), matrix[row].end(), 0);
    }

    static void clear_col(vector<vector<int>>& matrix, int col) {
        for(auto & row : matrix){
            row[col] = 0;
        }
    }
};
```