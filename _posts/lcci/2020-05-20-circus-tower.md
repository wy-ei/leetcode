---
title: 马戏团人塔
qid: 17.08
tags: [排序,二分查找,动态规划]
---


- 难度：Medium
- 题目链接：[https://leetcode-cn.com/problems/circus-tower-lcci/](https://leetcode-cn.com/problems/circus-tower-lcci/)


## 题目描述

来源于 [https://leetcode-cn.com/](https://leetcode-cn.com/)

<p>有个马戏团正在设计叠罗汉的表演节目，一个人要站在另一人的肩膀上。出于实际和美观的考虑，在上面的人要比下面的人矮一点且轻一点。已知马戏团每个人的身高和体重，请编写代码计算叠罗汉最多能叠几个人。</p>

<p><strong>示例：</strong></p>

<pre><strong>输入：</strong>height = [65,70,56,75,60,68] weight = [100,150,90,190,95,110]
<strong>输出：</strong>6
<strong>解释：</strong>从上往下数，叠罗汉最多能叠 6 层：(56,90), (60,95), (65,100), (68,110), (70,150), (75,190)</pre>

<p>提示：</p>

<ul>
	<li><code>height.length == weight.length &lt;= 10000</code></li>
</ul>


## 解法：

这里使用的是最长递增子序列的解题思路，关于最长递增子序列，可以参考[Longest Increasing Subsequence](../problem/300-longest-increasing-subsequence.md)

```c++
class Solution {
public:
    int bestSeqAtIndex(vector<int>& height, vector<int>& weight) {
        vector<vector<int>> nums;
        nums.reserve(height.size());
        for(size_t i=0;i<height.size();i++){
            nums.push_back({height[i], weight[i]});
        }
        sort(nums.begin(), nums.end(), [](auto& a, auto& b){
            if(a[0] < b[0]) return true;
            if(a[0] == b[0]) return a[1] > b[1];
            return false;
        });

        vector<int> dp;
        dp.push_back(nums[0][1]);
        for(size_t i=1;i<nums.size();i++){
            if(nums[i][1] > dp.back()){
                dp.push_back(nums[i][1]);
            }else{
                auto it = lower_bound(dp.begin(), dp.end(), nums[i][1]);
                *it = nums[i][1];
            }
        }
        return dp.size();
    }
};
```