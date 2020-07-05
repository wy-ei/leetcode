---
title: 水域大小
qid: 16.19
tags: [深度优先搜索,广度优先搜索]
---


- 难度：Medium
- 题目链接：[https://leetcode-cn.com/problems/pond-sizes-lcci/](https://leetcode-cn.com/problems/pond-sizes-lcci/)


## 题目描述

来源于 [https://leetcode-cn.com/](https://leetcode-cn.com/)

<p>你有一个用于表示一片土地的整数矩阵<code>land</code>，该矩阵中每个点的值代表对应地点的海拔高度。若值为0则表示水域。由垂直、水平或对角连接的水域为池塘。池塘的大小是指相连接的水域的个数。编写一个方法来计算矩阵中所有池塘的大小，返回值需要从小到大排序。</p>
<p><strong>示例：</strong></p>
<pre><strong>输入：</strong>
[
  [0,2,1,0],
  [0,1,0,1],
  [1,1,0,1],
  [0,1,0,1]
]
<strong>输出：</strong> [1,2,4]
</pre>
<p><strong>提示：</strong></p>
<ul>
<li><code>0 < len(land) <= 1000</code></li>
<li><code>0 < len(land[i]) <= 1000</code></li>
</ul>


## 解法：

深度优先搜索，对水域进行标记。只要从水域中的任何一点进入水域，在 dfs 退出时候，该水域就已经被完全标记了。因此，在 dfs 的时候可以维护一个计数器，dfs 内部对计数器累加，dfs 返回的时候就可以得到水域的面积了。

```c++
class Solution {
public:
    vector<int> pondSizes(vector<vector<int>>& land) {
        vector<int> ret;

        int n_rows = land.size();
        int n_cols = land.back().size();
        
        for(int i = 0; i < n_rows; i++){
            for(int j = 0; j < n_cols; j++){
                if(land[i][j] == 0){
                    int count = 0;
                    dfs(i, j, land, count);
                    ret.push_back(count);
                }
            }
        }

        sort(ret.begin(), ret.end());
        return ret;
    }
    
    void dfs(int row, int col, vector<vector<int>>& land, int& count){
        int n_rows = land.size();
        int n_cols = land.back().size();
        
        if(row < 0 || col < 0 || row == n_rows || col == n_cols || land[row][col] != 0){
            return;
        }
        
        count += 1;
        land[row][col] = 1;

        for(int offset_row=-1;offset_row<=1;offset_row++){
            for(int offset_col=-1;offset_col<=1;offset_col++){
                if(offset_row == 0 && offset_col == 0){
                    continue;
                }
                dfs(row + offset_row, col + offset_col, land, count);
            }
        }
    }
};
```