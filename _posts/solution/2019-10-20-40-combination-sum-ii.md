---
title: 组合总和 II
qid: 40
tags: [数组,回溯算法,深度优先搜索]
---


- 难度： 中等
- 通过率： 39.2%
- 题目链接：[https://leetcode-cn.com/problems/combination-sum-ii](https://leetcode-cn.com/problems/combination-sum-ii)


## 题目描述

来源于 [https://leetcode-cn.com/](https://leetcode-cn.com/)

<p>给定一个数组&nbsp;<code>candidates</code>&nbsp;和一个目标数&nbsp;<code>target</code>&nbsp;，找出&nbsp;<code>candidates</code>&nbsp;中所有可以使数字和为&nbsp;<code>target</code>&nbsp;的组合。</p>

<p><code>candidates</code>&nbsp;中的每个数字在每个组合中只能使用一次。</p>

<p><strong>说明：</strong></p>

<ul>
	<li>所有数字（包括目标数）都是正整数。</li>
	<li>解集不能包含重复的组合。&nbsp;</li>
</ul>

<p><strong>示例&nbsp;1:</strong></p>

<pre><strong>输入:</strong> candidates =&nbsp;<code>[10,1,2,7,6,1,5]</code>, target =&nbsp;<code>8</code>,
<strong>所求解集为:</strong>
[
  [1, 7],
  [1, 2, 5],
  [2, 6],
  [1, 1, 6]
]
</pre>

<p><strong>示例&nbsp;2:</strong></p>

<pre><strong>输入:</strong> candidates =&nbsp;[2,5,2,1,2], target =&nbsp;5,
<strong>所求解集为:</strong>
[
&nbsp; [1,2,2],
&nbsp; [5]
]</pre>


## 解法：

本题和 39 题 {% include post_link qid="39" %} 的区别在于本题中存在重复元素，且同一个元素不能多次使用。如果采用 39 题的解法，会出现重复。

此处只需要在 39 的基础上稍做改动即可。

1\. 跳过上次使用的数字：

```cpp
auto it = candidates.begin() + start + 1;
```

2\. 不使用重复元素：

```cpp
it = upper_bound(candidates.begin(), candidates.end(), *it);
```

3\. `dfs` 的第三个参数 `start` 指向下一个元素。


```cpp

class Solution {
public:
    vector<vector<int>> combinationSum2(vector<int>& candidates, int target) {
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
            dfs(candidates, path, result, it - candidates.begin() + 1, target - *it);
            path.pop_back();
            it = upper_bound(candidates.begin(), candidates.end(), *it);
        }
    }
};
```