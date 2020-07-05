---
title: 搜索旋转排序数组
qid: 33
tags: [数组,二分查找]
---


- 难度： 中等
- 通过率： 32.5%
- 题目链接：[https://leetcode.com/problems/search-in-rotated-sorted-array](https://leetcode.com/problems/search-in-rotated-sorted-array)


## 题目描述

来源于 [https://leetcode-cn.com/](https://leetcode-cn.com/)

<p>假设按照升序排序的数组在预先未知的某个点上进行了旋转。</p>

<p>( 例如，数组&nbsp;<code>[0,1,2,4,5,6,7]</code>&nbsp;可能变为&nbsp;<code>[4,5,6,7,0,1,2]</code>&nbsp;)。</p>

<p>搜索一个给定的目标值，如果数组中存在这个目标值，则返回它的索引，否则返回&nbsp;<code>-1</code>&nbsp;。</p>

<p>你可以假设数组中不存在重复的元素。</p>

<p>你的算法时间复杂度必须是&nbsp;<em>O</em>(log&nbsp;<em>n</em>) 级别。</p>

<p><strong>示例 1:</strong></p>

<pre><strong>输入:</strong> nums = [<code>4,5,6,7,0,1,2]</code>, target = 0
<strong>输出:</strong> 4
</pre>

<p><strong>示例&nbsp;2:</strong></p>

<pre><strong>输入:</strong> nums = [<code>4,5,6,7,0,1,2]</code>, target = 3
<strong>输出:</strong> -1</pre>


## 解法

有序数组旋转后，可以看做两个有序数组拼接起来了。如果能够把范围限定在其中一个数组内，就可以运行二分查找。

因为旋转后的前半部分中的值一定大于后半部分，且 `nums[0]` 是前半部分中最小的值。

因此 `nums[i] >= nums[0]` 说明 `i` 在前半部分。否则一定在右半部分。在二分查找时，根据 `nums[mid]` 和 `target` 的位置，来调整上下界。

当 target 和 `nums[mid]` 在同一侧时：

- 此时和常规的二分查找相同。
    
当 target 和`nums[mid]` 不在同一侧时：

- target 在左，`nums[mid]` 在右，需要调小 hi，即 hi = mid
- target 在右，`nums[mid]` 在左，需要调大 lo，即 lo = mid + 1

```c++
class Solution {
public:
    int search(vector<int>& nums, int target) {
        int lo = 0, hi = nums.size();
        while(lo < hi){
            int mid = lo + (hi - lo) / 2;
            // 同一侧
            if((nums[mid] < nums[0]) == (target < nums[0])){
                if(nums[mid] > target){
                    hi = mid;
                }else if(nums[mid] < target){
                    lo = mid + 1;
                }else{
                    return mid;
                }
            }else{
                if(nums[mid] > target){
                    lo = mid +1;
                }else{
                    hi = mid;
                }
            }
        }
        return -1;
    }
};
```