## 53 - I. 在排序数组中查找数字 I

- 难度：Easy
- 题目链接：[https://leetcode-cn.com/problems/zai-pai-xu-shu-zu-zhong-cha-zhao-shu-zi-lcof/](https://leetcode-cn.com/problems/zai-pai-xu-shu-zu-zhong-cha-zhao-shu-zi-lcof/)


## 题目描述

来源于 [https://leetcode-cn.com/](https://leetcode-cn.com/)

<p>统计一个数字在排序数组中出现的次数。</p>

<p>&nbsp;</p>

<p><strong>示例 1:</strong></p>

<pre><strong>输入:</strong> nums = [<code>5,7,7,8,8,10]</code>, target = 8
<strong>输出:</strong> 2</pre>

<p><strong>示例&nbsp;2:</strong></p>

<pre><strong>输入:</strong> nums = [<code>5,7,7,8,8,10]</code>, target = 6
<strong>输出:</strong> 0</pre>

<p>&nbsp;</p>

<p><strong>限制：</strong></p>

<p><code>0 &lt;= 数组长度 &lt;= 50000</code></p>

<p>&nbsp;</p>

<p><strong>注意：</strong>本题与主站 34 题相同（仅返回值不同）：<a href="https://leetcode-cn.com/problems/find-first-and-last-position-of-element-in-sorted-array/">https://leetcode-cn.com/problems/find-first-and-last-position-of-element-in-sorted-array/</a></p>


## 解法：

在排序数组中寻找某个数的 `lower_bound` 和 `upper_bound`，然后计算两者之差，就能知道这个数出现了多少次。

```c++
class Solution {
public:
    int search(vector<int>& nums, int target) {
        auto it1 = lower_bound(nums.begin(), nums.end(), target);
        auto it2 = upper_bound(it1, nums.end(), target);
        return distance(it1, it2);
    }
};
```

自己动手实现 `lower_bound` 和 `upper_bound` 如下：

```c++
int lower_bound(const vector<int> &nums, int val){
    int lo = 0, hi = nums.size();
    
    while(lo < hi){
        int mid = lo + (hi - lo) / 2;
        if(nums[mid] < val){
            lo = mid + 1;
        }else{
            hi = mid;
        }
    }
    return lo;
}

int upper_bound(const vector<int> &nums, int val){
    int lo = 0, hi = nums.size();

    while(lo < hi){
        int mid = lo + (hi - lo) / 2;
        if(nums[mid] <= val){
            lo = mid + 1;
        }else{
            hi = mid;
        }
    }
    return lo;
}


class Solution {
public:
    int search(vector<int>& nums, int target) {
        return upper_bound(nums, target) - lower_bound(nums, target);
    }
};
```

实现 `lower_bound` 和 `upper_bound` 的关键在于更新 `lo` 的条件。`lower_bound` 返回的是第一个大于等于 `val` 的值的下标，因此只有 `nums[mid] < val` 的时候，才能设置 `low = mid + 1`。

`lower_bound` 返回第一个大于 `val` 的值的下标，因此在 `nums[mid] <= val` 的时候，可以让 `lo` 指向 `mid` 后一个元素。