---
title: 八皇后
qid: 08.12
tags: [回溯算法]
---


- 难度：Hard
- 题目链接：[https://leetcode-cn.com/problems/eight-queens-lcci/](https://leetcode-cn.com/problems/eight-queens-lcci/)


## 题目描述

来源于 [https://leetcode-cn.com/](https://leetcode-cn.com/)

<p>设计一种算法，打印 N 皇后在 N &times; N 棋盘上的各种摆法，其中每个皇后都不同行、不同列，也不在对角线上。这里的&ldquo;对角线&rdquo;指的是所有的对角线，不只是平分整个棋盘的那两条对角线。</p>

<p><strong>注意：</strong>本题相对原题做了扩展</p>

<p><strong>示例:</strong></p>

<pre><strong> 输入</strong>：4
<strong> 输出</strong>：[[&quot;.Q..&quot;,&quot;...Q&quot;,&quot;Q...&quot;,&quot;..Q.&quot;],[&quot;..Q.&quot;,&quot;Q...&quot;,&quot;...Q&quot;,&quot;.Q..&quot;]]
<strong> 解释</strong>: 4 皇后问题存在如下两个不同的解法。
[
&nbsp;[&quot;.Q..&quot;, &nbsp;// 解法 1
&nbsp; &quot;...Q&quot;,
&nbsp; &quot;Q...&quot;,
&nbsp; &quot;..Q.&quot;],

&nbsp;[&quot;..Q.&quot;, &nbsp;// 解法 2
&nbsp; &quot;Q...&quot;,
&nbsp; &quot;...Q&quot;,
&nbsp; &quot;.Q..&quot;]
]
</pre>


## 解法：

又一个 dfs，为每一行选择一个放 `Q` 的位置，至于选那个位置需要考虑该位置上放 `Q` 是否与已放置的行冲突。

```c++
class Solution {
public:
    vector<vector<string>> solveNQueens(int n) {
        vector<string> board(n, string(n, '.'));
        vector<vector<string>> result;
        dfs(board, 0, result);
        return result;
    }

    void dfs(vector<string>& board, int row, vector<vector<string>>& result){
        int n = board.size();
        if(n == row){
            result.push_back(board);
            return;
        }
        for(int col = 0; col < n; col++){
            if(!conflict(board, row, col)){
                board[row][col] = 'Q';
                dfs(board, row + 1, result);
                board[row][col] = '.';
            }
        }
    }

    bool conflict(const vector<string>& board, int row, int col){
        int n = board.size();
        for(int i = 0; i < row; i++){
            if(board[i][col] == 'Q') return true;
            int j = col - (row - i);
            if(j >= 0 && board[i][j] == 'Q') return true;
            j = col + (row - i);
            if(j < n && board[i][j] == 'Q') return true;
        }
        return false;
    }
};
```