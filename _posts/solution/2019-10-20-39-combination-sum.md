---
title: 组合总和
qid: 39
tags: [数组,回溯算法,深度优先搜索]
---


- 难度： 中等
- 通过率： 45.4%
- 题目链接：[https://leetcode-cn.com/problems/combination-sum](https://leetcode-cn.com/problems/combination-sum)


## 题目描述

来源于 [https://leetcode-cn.com/](https://leetcode-cn.com/)

<p>给定一个<strong>无重复元素</strong>的数组&nbsp;<code>candidates</code>&nbsp;和一个目标数&nbsp;<code>target</code>&nbsp;，找出&nbsp;<code>candidates</code>&nbsp;中所有可以使数字和为&nbsp;<code>target</code>&nbsp;的组合。</p>

<p><code>candidates</code>&nbsp;中的数字可以无限制重复被选取。</p>

<p><strong>说明：</strong></p>

<ul>
	<li>所有数字（包括&nbsp;<code>target</code>）都是正整数。</li>
	<li>解集不能包含重复的组合。&nbsp;</li>
</ul>

<p><strong>示例&nbsp;1:</strong></p>

<pre><strong>输入:</strong> candidates = <code>[2,3,6,7], </code>target = <code>7</code>,
<strong>所求解集为:</strong>
[
  [7],
  [2,2,3]
]
</pre>

<p><strong>示例&nbsp;2:</strong></p>

<pre><strong>输入:</strong> candidates = [2,3,5]<code>, </code>target = 8,
<strong>所求解集为:</strong>
[
&nbsp; [2,2,2,2],
&nbsp; [2,3,3],
&nbsp; [3,5]
]</pre>


## 解法：

采用深度优先搜索来搜索解空间。先对数组由小达大排序，每次取一个数字，然后把 target 减掉此值，然后在此数及之后的数中继续寻找。

对数组进行排序，是为了避免重复，选取的下一个数字必须等于等于前一个。这样就不会出现 `1 + 2 = 3` 和 `2 + 1 = 3` 这样的重复组合了。

```cpp
class Solution {
public:
    vector<vector<int>> combinationSum(vector<int>& candidates, int target) {
        sort(candidates.begin(), candidates.end());
        vector<vector<int>> result;
        vector<int> path; // 中间结果
        dfs(candidates, path, result, 0, target);
        return result;
    }

    void dfs(const vector<int>& candidates, vector<int>& path,
                vector<vector<int>>& result, size_t start, int target){
        
        if(target == 0){
            result.push_back(path);
        }

        auto it = candidates.begin() + start; 
        while(it != candidates.end()){
            if(target < *it){
                return;
            }
            path.push_back(*it);
            dfs(candidates, path, result, it - candidates.begin(), target - *it);
            path.pop_back();
            ++it
        }
    }
};
```