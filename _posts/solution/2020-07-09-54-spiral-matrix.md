---
title: 螺旋矩阵
qid: 54
tag: [数组]
---

- 难度： 中等
- 通过率： 29.0%
- 题目链接：[https://leetcode-cn.com/problems/spiral-matrix](https://leetcode-cn.com/problems/spiral-matrix)


## 题目描述

来源于 [https://leetcode-cn.com/](https://leetcode-cn.com/)

<p>给定一个包含&nbsp;<em>m</em> x <em>n</em>&nbsp;个元素的矩阵（<em>m</em> 行, <em>n</em> 列），请按照顺时针螺旋顺序，返回矩阵中的所有元素。</p>

<p><strong>示例&nbsp;1:</strong></p>

<pre><strong>输入:</strong>
[
 [ 1, 2, 3 ],
 [ 4, 5, 6 ],
 [ 7, 8, 9 ]
]
<strong>输出:</strong> [1,2,3,6,9,8,7,4,5]
</pre>

<p><strong>示例&nbsp;2:</strong></p>

<pre><strong>输入:</strong>
[
  [1, 2, 3, 4],
  [5, 6, 7, 8],
  [9,10,11,12]
]
<strong>输出:</strong> [1,2,3,4,8,12,11,10,9,5,6,7]
</pre>


## 解法：

维护 row 和 col 的范围，然后分别打印矩阵的四个边，而后缩小范围。

打印四个方向的时候，范围不同。上边，打印完整一行。右侧，大于 `row_lo+1` 至 `row_hi`。下边，大于 `col_hi-1` 至 `col_lo`。左侧，打印 `row_hi-1` 至 `row_lo + 1`。

```
  +-------------+
  * * * * * * * * 
+ * * * * * * * * +
| * * * * * * * * |
| * * * * * * * * |
| * * * * * * * * |
| * * * * * * * * |
| * * * * * * * * |
+ * * * * * * * * |
  * * * * * * * * +
  +-----------+
```

如果矩阵仅剩下一行或者一列，打印完上边和右侧，矩阵就全部打印完了。如果采用下面这样的策略：

```
  +-----------+
  * * * * * * * * +
+ * * * * * * * * |
| * * * * * * * * |
| * * * * * * * * |
| * * * * * * * * |
| * * * * * * * * |
| * * * * * * * * |
| * * * * * * * * +
+ * * * * * * * * 
    +-----------+
```

这里区间采用了左闭右开，看起来相当的统一。但是会出现一个棘手的问题，只余下单个元素的时候，`row_lo == row_hi` 且 `col_lo == col_hi`，余下的一个元素无法打印出来。


```c++
class Solution {
public:
    vector<int> spiralOrder(vector<vector<int>>& matrix) {
        vector<int> ret;
        if(matrix.empty() || matrix[0].empty()){
            return ret;
        }
        int n_rows = matrix.size();
        int n_cols =  matrix[0].size();
        int row_lo = 0, row_hi = n_rows - 1;
        int col_lo = 0, col_hi = n_cols - 1;
        
        while(row_lo <= row_hi && col_lo <= col_hi){
            for(int i=col_lo;i<=col_hi;i++){
                ret.push_back(matrix[row_lo][i]);
            }
            
            for(int i=row_lo+1;i<=row_hi;i++){
                ret.push_back(matrix[i][col_hi]);
            }
            
			// 仅有一排或者一列的时候
            if(row_lo == row_hi || col_lo == col_hi){
                break;
            }

            for(int i=col_hi-1;i>=col_lo;i--){
                ret.push_back(matrix[row_hi][i]);
            }


            for(int i=row_hi-1;i>row_lo;i--){
                ret.push_back(matrix[i][col_lo]);
            }

            row_lo += 1;
            row_hi -= 1;
            col_lo += 1;
            col_hi -= 1;
        }

        return ret;
    }
};
```