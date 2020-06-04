## 300. Longest Increasing Subsequence

- 难度： 中等
- 通过率： 39.9%
- 题目链接：[https://leetcode.com/problems/longest-increasing-subsequence](https://leetcode.com/problems/longest-increasing-subsequence)


## 题目描述

来源于 [https://leetcode-cn.com/](https://leetcode-cn.com/)

<p>给定一个无序的整数数组，找到其中最长上升子序列的长度。</p>

<p><strong>示例:</strong></p>

<pre><strong>输入:</strong> <code>[10,9,2,5,3,7,101,18]
</code><strong>输出: </strong>4 
<strong>解释: </strong>最长的上升子序列是&nbsp;<code>[2,3,7,101]，</code>它的长度是 <code>4</code>。</pre>

<p><strong>说明:</strong></p>

<ul>
	<li>可能会有多种最长上升子序列的组合，你只需要输出对应的长度即可。</li>
	<li>你算法的时间复杂度应该为&nbsp;O(<em>n<sup>2</sup></em>) 。</li>
</ul>

<p><strong>进阶:</strong> 你能将算法的时间复杂度降低到&nbsp;O(<em>n</em> log <em>n</em>) 吗?</p>


## 解法一：动态规划

动态规划，`dp[i]` 表示 `i` 之前的元素构成的最长上升子序列的长度。对于 `nums[i]` 只需要在 `i` 前面寻找小于 `nums[i]` 的所有数 `nums[j]`。其中 `dp[j] + 1` 的最大值就是新的最长上升子序列的长度。

```c++
class Solution {
public:
    int lengthOfLIS(vector<int>& nums) {
        if(nums.empty()) return 0;

        vector<int> dp(nums.size(), 0);
        for(int i=0;i<nums.size();i++){
            int max_len = 0;
            for(int j=0;j<i;j++){
                if(nums[i] > nums[j]){
                    max_len = max(max_len, dp[j]);
                }
            }
            dp[i] = 1 + max_len;
        }
        
        return *max_element(dp.begin(), dp.end());
    }
};
```

## 解法二：二分查找

从左到右遍历数组，使用数组记录下不同长度的上升子序列的最后一个元素的最小值。

对于例子 `[10,9,2,5,3,7,101,18]` 而言，`10` `9` `2` 都构成长度为 1 的上升子序列，为了使子序列尽可能长，保留最小的即可。得到数组：`[2]`

下一个元素 `5` 比 `2` 大，因此可以构成子序列 `[2,5]`。

下一个元素 `3` 也只能构成长度为 2 的子序列，而且 3 比 5 小，因此构成子序列 `[2,3]`。

如此结果数组中，每个下标 i 中的值，就是长度为 i+1 的子序列中尾段最小的值。因此，新来一个元素，可以在这数组中二分查找，找到当前元素能够构成的最长子序列。并更新尾段的值，使子序列中的最大值尽可能小。

```c++
class Solution {
public:
    int lengthOfLIS(vector<int>& nums) {
        if(nums.empty()) return 0;

        vector<int> dp;
        dp.push_back(nums[0]);
        for(int i=1;i<nums.size();i++){
            if(nums[i] > dp.back()){
                dp.push_back(nums[i]);
            }else{
                auto it = lower_bound(dp.begin(), dp.end(), nums[i]);
                *it = nums[i];
            }
        }
        
        return dp.size();
    }
};
```