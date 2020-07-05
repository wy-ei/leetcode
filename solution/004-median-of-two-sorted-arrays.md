## 4. Median of Two Sorted Arrays

- 难度： 困难
- 通过率： 24.9%
- 题目链接：[https://leetcode.com/problems/median-of-two-sorted-arrays](https://leetcode.com/problems/median-of-two-sorted-arrays)


## 题目描述

来源于 [https://leetcode-cn.com/](https://leetcode-cn.com/)

<p>给定两个大小为 m 和 n 的有序数组&nbsp;<code>nums1</code> 和&nbsp;<code>nums2</code>。</p>

<p>请你找出这两个有序数组的中位数，并且要求算法的时间复杂度为&nbsp;O(log(m + n))。</p>

<p>你可以假设&nbsp;<code>nums1</code>&nbsp;和&nbsp;<code>nums2</code>&nbsp;不会同时为空。</p>

<p><strong>示例 1:</strong></p>

<pre>nums1 = [1, 3]
nums2 = [2]

则中位数是 2.0
</pre>

<p><strong>示例 2:</strong></p>

<pre>nums1 = [1, 2]
nums2 = [3, 4]

则中位数是 (2 + 3)/2 = 2.5
</pre>


## 解法1：简单粗暴解

是合并两个数组，然后计算中位数。时间复杂度为 `O(n+m)`。实际操作的时候不需要真正进行合并操作，只需要维护一个计数器，找到中间的那两个元素即可。

```c++
class Solution {
public:
    double findMedianSortedArrays(vector<int>& nums1, vector<int>& nums2) {
        int mid_len = (nums1.size() + nums2.size()) / 2;

        int a = 0, b = 0;
        int i = 0, j = 0;
        int count = 0;
        while(count <= mid_len){
            count++;
            a = b;
            if(i == nums1.size()){
                b = nums2[j++];
            }else if(j == nums2.size()){
                b = nums1[i++];
            }else if(nums1[i] < nums2[j]){
                b = nums1[i++];
            }else{
                b = nums2[j++];
            }
        }

        if((nums1.size() + nums2.size()) % 2 == 0){
            return (a + b) / 2.0;
        }else{
            return b;
        }
    }
};
```

## 解法2：二分查找

TODO