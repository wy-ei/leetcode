---
title: 迷路的机器人
qid: 08.02
tags: [动态规划]
---


- 难度：Medium
- 题目链接：[https://leetcode-cn.com/problems/robot-in-a-grid-lcci/](https://leetcode-cn.com/problems/robot-in-a-grid-lcci/)


## 题目描述

来源于 [https://leetcode-cn.com/](https://leetcode-cn.com/)

<p>设想有个机器人坐在一个网格的左上角，网格 r 行 c 列。机器人只能向下或向右移动，但不能走到一些被禁止的网格（有障碍物）。设计一种算法，寻找机器人从左上角移动到右下角的路径。</p>

<p><img src="https://assets.leetcode-cn.com/aliyun-lc-upload/uploads/2018/10/22/robot_maze.png" style="height: 183px; width: 400px;"></p>

<p>网格中的障碍物和空位置分别用 <code>1</code> 和 <code>0</code> 来表示。</p>

<p>返回一条可行的路径，路径由经过的网格的行号和列号组成。左上角为 0 行 0 列。如果没有可行的路径，返回空数组。</p>

<p><strong>示例&nbsp;1:</strong></p>

<pre><strong>输入:
</strong>[
&nbsp; [<strong>0</strong>,<strong>0</strong>,<strong>0</strong>],
&nbsp; [0,1,<strong>0</strong>],
&nbsp; [0,0,<strong>0</strong>]
]
<strong>输出:</strong> [[0,0],[0,1],[0,2],[1,2],[2,2]]
<strong>解释: 
</strong>输入中标粗的位置即为输出表示的路径，即
0行0列（左上角） -&gt; 0行1列 -&gt; 0行2列 -&gt; 1行2列 -&gt; 2行2列（右下角）</pre>

<p><strong>说明：</strong><em>r</em>&nbsp;和 <em>c </em>的值均不超过 100。</p>


## 解法一：深度优先遍历

从左上角开始深度优先遍历，遍历过程中标记下自己已经访问过的点。深度优先遍历找到第一个可行的路径后，其后的所有遍历全都立刻退出，避免多余的运算。

在二维空间做 dfs 时，常常在 dfs 之前标记该点已访问，在退出时取消标记。但在此处是不需要取消标记的。取消标记通常是在二维空间中寻找一个路径，此处只要一个点被访问过，那么肯定不用在访问了。

```c++
public:
    vector<vector<int>> pathWithObstacles(vector<vector<int>>& obstacleGrid) {
        vector<vector<int>> result;

        int n_rows = obstacleGrid.size();
        if(n_rows == 0) return result;
        int n_cols = obstacleGrid.back().size();
        if(n_cols == 0) return result;

        vector<vector<int>> visited(n_rows, vector<int>(n_cols, 0));
        dfs(0, 0, result, obstacleGrid, visited);
        return result;
    }

    bool dfs(int row, int col, vector<vector<int>>& result,
             vector<vector<int>>& grid, vector<vector<int>>& visited){

        int n_rows = grid.size();
        int n_cols = grid.back().size();

        if(row == n_rows || col == n_cols) return false;
        if(visited[row][col] == 1) return false;
        if(grid[row][col] == 1) return false;

        result.push_back({row, col});
        if(row == n_rows-1 && col == n_cols-1){
            return true;
        }
        visited[row][col] = 1;

        bool found = dfs(row+1, col, result, grid, visited)
                     || dfs(row, col+1, result, grid, visited);
        if(!found){
            result.pop_back();
        }
        return found;
    }
};
```

**总结**

DFS 和树的遍历是一个道理，如果是寻找路径，那就采用类似先序遍历的方法：

```c++
void dfs(){
    // 检查退出条件
    
    // 处理当前点

    // 标记当前点已经被访问过 [可选]
    
    // dfs(下一个位置) 可能有多个位置 (上下左右)
    // 判断是否退出

    // 取消标记当前点 [可选]
}
```

如果需要用后续的节点的搜索结果来得到一个新的结果，通常采用类似后序遍历的方法：

```c++
int dfs(){
    // 检查退出条件，退出时返回最基本的情况的结果
    
    // 标记当前点已经被访问过 [可选]
    
    // 结果 = dfs(下一个位置) 可能有多个位置 (上下左右)
    // 新的结果 = f(结果)

    // 取消标记当前点 [可选]
    // return 新的结果
}
```

## 解法二：动态规划

从右下角开始，记录下从当前点到终点的路径上，从当前点出发可选的下一个点的坐标，可以是其右边和下边的某个点，或者没有可行的点（意味着从该点不能达到终点）。记录完成后，从左上角不断地找到下一个点的左边，最终就达到了终点。

这里我在原障碍数组中来标记坐标，把左边信息编码到一个整数中 `code = row * n_cols + col + 1`，然后存储在障碍数组中，但是 code 有可能是 1，此时会和障碍信息混淆，因此把 code 取负，然后存储。

```c++
class Solution {
public:
    vector<vector<int>> pathWithObstacles(vector<vector<int>>& obstacleGrid) {
        vector<vector<int>> path;
        int n_rows = obstacleGrid.size();
        if(n_rows == 0) return path;
        int n_cols = obstacleGrid.back().size();
        if(n_cols == 0) return path;
        if(obstacleGrid[0][0] == 1) return path;
        if(obstacleGrid.back().back() == 1) return path;
        
        obstacleGrid.back().back() = -1;
        for(int row = n_rows-1; row >= 0; row--){
            for(int col = n_cols-1; col >= 0; col--){
                if(obstacleGrid[row][col] == 1){
                    continue;
                }
                if(col + 1 < n_cols && obstacleGrid[row][col+1] < 0){
                    int code = row * n_cols + col + 1;
                    obstacleGrid[row][col] = -code;
                }
                else if(row + 1 < n_rows && obstacleGrid[row+1][col] < 0){
                    int code = (row + 1) * n_cols + col;
                    obstacleGrid[row][col] = -code;
                }
            }
        }

        int row = 0, col = 0;
        while(true){
            path.push_back(vector<int>{row, col});
            if(row == n_rows - 1 && col == n_cols - 1){
                break;
            }
            int code = obstacleGrid[row][col];
            if(code == 0 || code == 1) break;
            row = (-code) / n_cols;
            col = (-code) % n_cols;
        }

        
        if(path.size() == (n_rows + n_cols - 1)){
            return path;
        }else{
            return vector<vector<int>>();
        }
    }
};
```