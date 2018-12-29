## 1. Two Sum


- 难度： 简单
- 通过率： 39.6%
- 题目链接：[https://leetcode.com/problems/two-sum](https://leetcode.com/problems/two-sum)

<p>There are two sorted arrays <b>nums1</b> and <b>nums2</b> of size m and n respectively.</p>

<p>Find the median of the two sorted arrays. The overall run time complexity should be O(log (m+n)).</p>

<p>You may assume <strong>nums1</strong> and <strong>nums2</strong>&nbsp;cannot be both empty.</p>



### 解法：

需要在数组中寻找两个数使其和为 target，可以将数组中的值存放在 map 中并记录下标，这样在遍历的过程中，如果当前元素为 a，那么寻找 target - a 的值时就能够得到加速。


```python
class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        mp = {}
        for i, num in enumerate(nums):
            other = target - num
            if other in mp:
                return [mp[other], i]
            else:
                mp[num] = i
                
        return [0, 0]
```