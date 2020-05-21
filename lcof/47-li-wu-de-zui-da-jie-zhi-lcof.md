## 47. 礼物的最大价值

- 难度：Medium
- 题目链接：[https://leetcode-cn.com/problems/li-wu-de-zui-da-jie-zhi-lcof/](https://leetcode-cn.com/problems/li-wu-de-zui-da-jie-zhi-lcof/)


## 题目描述

来源于 [https://leetcode-cn.com/](https://leetcode-cn.com/)

<p>在一个 m*n 的棋盘的每一格都放有一个礼物，每个礼物都有一定的价值（价值大于 0）。你可以从棋盘的左上角开始拿格子里的礼物，并每次向右或者向下移动一格、直到到达棋盘的右下角。给定一个棋盘及其上面的礼物的价值，请计算你最多能拿到多少价值的礼物？</p>

<p>&nbsp;</p>

<p><strong>示例 1:</strong></p>

<pre><strong>输入:</strong> 
<code>[
&nbsp; [1,3,1],
&nbsp; [1,5,1],
&nbsp; [4,2,1]
]</code>
<strong>输出:</strong> <code>12
</code><strong>解释:</strong> 路径 1&rarr;3&rarr;5&rarr;2&rarr;1 可以拿到最多价值的礼物</pre>

<p>&nbsp;</p>

<p>提示：</p>

<ul>
    <li><code>0 &lt; grid.length &lt;= 200</code></li>
    <li><code>0 &lt; grid[0].length &lt;= 200</code></li>
</ul>


## 解法：

用动态规划，计算在每个位置上可以得到的礼物价值总和的最大值。

```c++
class Solution {
public:
    int maxValue(vector<vector<int>>& grid) {
        int n_rows = grid.size();
        int n_cols = grid[0].size();
        for(int row=0;row<n_rows;row++){
            for(int col=0;col<n_cols;col++){
                int n = 0;
                if(row-1 >= 0){
                    n = grid[row-1][col];
                }
                if(col-1 >= 0){
                    n = max(n, grid[row][col-1]);
                }
                grid[row][col] += n;
            }
        }
        return grid.back().back();
    }
};
```

上面这种方法，使用原矩阵作为动态规划的 dp 矩阵，这会修改输入数据，如果要求不修改输入。那就需要创建一个 dp 矩阵。上面的方法中 dp 的大小是 m*n。但其实可以使用一维的向量来存储中间值。


使用一个向量 dp，存储在每一列上所能得到的最大值。因为在每个点上，移动方向只能是向右或者向下。如果向右，那么 `dp[i] = dp[i-1] + grid[row][i]`。如果向下移动，那么 `dp[i] = dp[i] + grid[row][i]`。

所以在每个点上 `(row, i)`，只需要做如下更新 `dp[i] = max(dp[i], dp[i-1]) + grid[row][i]`。

```c++
class Solution {
public:
    int maxValue(vector<vector<int>>& grid) {
        int n_rows = grid.size();
        int n_cols = grid[0].size();
        vector<int> dp(n_cols, 0);
        for(int row=0;row<n_rows;row++){
            for(int col=0;col<n_cols;col++){
                int n = 0;
                if(col > 0){
                    n = max(dp[col], dp[col-1]);
                }else{
                    n = dp[col];
                }
                dp[col] = n + grid[row][col];
            }
        }
        return dp.back();
    }
};
```