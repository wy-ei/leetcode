---
title: 前 K 个高频元素
qid: 347
tag: [堆, 哈希表]
---

- 难度： 中等
- 通过率： 52.3%
- 题目链接：[https://leetcode-cn.com/problems/top-k-frequent-elements](https://leetcode-cn.com/problems/top-k-frequent-elements)


## 题目描述

来源于 [https://leetcode-cn.com/](https://leetcode-cn.com/)

<p>给定一个非空的整数数组，返回其中出现频率前&nbsp;<strong><em>k&nbsp;</em></strong>高的元素。</p>

<p><strong>示例 1:</strong></p>

<pre><strong>输入: </strong>nums = [1,1,1,2,2,3], k = 2
<strong>输出: </strong>[1,2]
</pre>

<p><strong>示例 2:</strong></p>

<pre><strong>输入: </strong>nums = [1], k = 1
<strong>输出: </strong>[1]</pre>

<p><strong>说明：</strong></p>

<ul>
	<li>你可以假设给定的&nbsp;<em>k&nbsp;</em>总是合理的，且 1 &le; k &le; 数组中不相同的元素的个数。</li>
	<li>你的算法的时间复杂度<strong>必须</strong>优于 O(<em>n</em> log <em>n</em>) ,&nbsp;<em>n&nbsp;</em>是数组的大小。</li>
</ul>


## 解法：

```c++
class Solution {
public:
    vector<int> topKFrequent(vector<int>& nums, int k) {
        unordered_map<int,int> mapping;
        for(int n: nums){
            mapping[n]++;
        }
        priority_queue<int, vector<int>, function<bool(int,int)>> pq([&mapping](int k1, int k2){
            return mapping[k1] > mapping[k2];
        });
        for(auto &item: mapping){
            pq.push(item.first);
            if(pq.size() > k){
                pq.pop();
            }
        }
        vector<int> result;
        while(!pq.empty()){
            result.push_back(pq.top());
            pq.pop();
        }
        return result;
    }
};
```